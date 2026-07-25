#!/usr/bin/env python3
"""
agent-token-saas 后端 v0.1
- FastAPI
- 用 Kimi (开发) / OpenRouter (生产) 调 AI
- JWT 认证
- Token 钱包（SQLite/Postgres）
"""
import os
import sys
import time
import json
import sqlite3
import hashlib
import secrets
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import jwt
import httpx
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr

# === 配置 ===
SECRET_KEY = os.environ.get('JWT_SECRET', 'dev-secret-change-in-prod-' + secrets.token_hex(8))
JWT_ALGO = 'HS256'
JWT_EXPIRE_DAYS = 30

# AI provider 配置
# 开发用 DeepSeek（你机器已经有 key，最稳）
# 生产用 OpenRouter（海外服务器）
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')
DEEPSEEK_URL = 'https://api.deepseek.com/v1/chat/completions'
DEEPSEEK_MODEL = os.environ.get('DEEPSEEK_MODEL', 'deepseek-v4-flash')

KIMI_API_KEY = os.environ.get('MOONSHOT_API_KEY', '')
KIMI_URL = 'https://api.moonshot.cn/v1/chat/completions'
KIMI_MODEL = 'kimi-k2-6'

OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')
OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_MODEL = 'deepseek/deepseek-chat-v3'

# 当前用哪个 provider
USE_PROVIDER = os.environ.get('AI_PROVIDER', 'deepseek')  # 'deepseek' or 'kimi' or 'openrouter'

DB_PATH = Path(os.environ.get('DB_PATH', './data.db'))

# Token 价格（每 1K tokens）
TOKEN_PRICE = {
    'deepseek': 0.00014,  # DeepSeek V3 价格
    'kimi': 0.000012,  # Kimi 价格
    'openrouter': 0.00027,  # $0.27/1M input
}

# === DB 初始化 ===
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            token_balance INTEGER DEFAULT 50000,
            created_at TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            prompt_tokens INTEGER,
            completion_tokens INTEGER,
            total_tokens INTEGER,
            model TEXT,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# === Models ===
class RegisterReq(BaseModel):
    email: EmailStr
    password: str


class LoginReq(BaseModel):
    email: EmailStr
    password: str


class ChatReq(BaseModel):
    message: str
    model: Optional[str] = None


class ChatResp(BaseModel):
    reply: str
    tokens_used: int
    token_balance: int


# === Auth ===
def create_token(user_id: int) -> str:
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=JWT_EXPIRE_DAYS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGO)


def verify_token(token: str) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGO])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, 'token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(401, 'invalid token')


async def current_user(authorization: str = Header(None)) -> dict:
    if not authorization or not authorization.startswith('Bearer '):
        raise HTTPException(401, 'missing token')
    token = authorization.replace('Bearer ', '')
    user_id = verify_token(token)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if not user:
        raise HTTPException(401, 'user not found')
    return dict(user)


# === AI Provider ===
async def call_ai(message: str, model: Optional[str] = None) -> dict:
    """调 AI，返回 {reply, prompt_tokens, completion_tokens, total_tokens}"""
    if USE_PROVIDER == 'deepseek':
        return await call_deepseek(message, model or DEEPSEEK_MODEL)
    elif USE_PROVIDER == 'kimi':
        return await call_kimi(message, model or KIMI_MODEL)
    else:
        return await call_openrouter(message, model or OPENROUTER_MODEL)


async def call_deepseek(message: str, model: str) -> dict:
    """调 DeepSeek API"""
    if not DEEPSEEK_API_KEY:
        raise HTTPException(500, 'DEEPSEEK_API_KEY not configured')

    headers = {
        'Authorization': 'Bearer ' + DEEPSEEK_API_KEY,
        'Content-Type': 'application/json',
    }
    body = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': 'You are a helpful AI assistant. Be concise and direct.'},
            {'role': 'user', 'content': message}
        ],
        'temperature': 0.7,
        'max_tokens': 2000,
    }

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(DEEPSEEK_URL, headers=headers, json=body)
        r.raise_for_status()
        result = r.json()

    return {
        'reply': result['choices'][0]['message']['content'].strip(),
        'prompt_tokens': result['usage']['prompt_tokens'],
        'completion_tokens': result['usage']['completion_tokens'],
        'total_tokens': result['usage']['total_tokens'],
    }


async def call_kimi(message: str, model: str) -> dict:
    """调 Kimi API"""
    if not KIMI_API_KEY:
        raise HTTPException(500, 'KIMI_API_KEY not configured')

    headers = {
        'Authorization': f'Bearer {KIMI_API_KEY}',
        'Content-Type': 'application/json',
    }
    body = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': 'You are a helpful AI assistant. Be concise and direct.'},
            {'role': 'user', 'content': message}
        ],
        'temperature': 0.7,
        'max_tokens': 2000,
    }

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(KIMI_URL, headers=headers, json=body)
        r.raise_for_status()
        result = r.json()

    return {
        'reply': result['choices'][0]['message']['content'].strip(),
        'prompt_tokens': result['usage']['prompt_tokens'],
        'completion_tokens': result['usage']['completion_tokens'],
        'total_tokens': result['usage']['total_tokens'],
    }


async def call_openrouter(message: str, model: str) -> dict:
    """调 OpenRouter API"""
    if not OPENROUTER_API_KEY:
        raise HTTPException(500, 'OPENROUTER_API_KEY not configured')

    headers = {
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'Content-Type': 'application/json',
    }
    body = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': 'You are a helpful AI assistant. Be concise and direct.'},
            {'role': 'user', 'content': message}
        ],
        'temperature': 0.7,
        'max_tokens': 2000,
    }

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(OPENROUTER_URL, headers=headers, json=body)
        r.raise_for_status()
        result = r.json()

    return {
        'reply': result['choices'][0]['message']['content'].strip(),
        'prompt_tokens': result['usage']['prompt_tokens'],
        'completion_tokens': result['usage']['completion_tokens'],
        'total_tokens': result['usage']['total_tokens'],
    }


# === App ===
app = FastAPI(title='Agent Token SaaS', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # 开发环境，生产要限制
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
def startup():
    init_db()


@app.get('/health')
def health():
    return {'status': 'ok', 'provider': USE_PROVIDER}


# === Auth Endpoints ===
@app.post('/api/auth/register')
def register(req: RegisterReq):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 检查邮箱
    existing = c.execute('SELECT id FROM users WHERE email = ?', (req.email,)).fetchone()
    if existing:
        conn.close()
        raise HTTPException(400, 'email already registered')

    # 创建
    c.execute(
        'INSERT INTO users (email, password_hash, token_balance, created_at) VALUES (?, ?, ?, ?)',
        (req.email, hash_password(req.password), 50000, datetime.utcnow().isoformat())
    )
    user_id = c.lastrowid
    conn.commit()
    conn.close()

    return {
        'user_id': user_id,
        'email': req.email,
        'token': create_token(user_id),
        'token_balance': 50000,
    }


@app.post('/api/auth/login')
def login(req: LoginReq):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    user = conn.execute(
        'SELECT * FROM users WHERE email = ?',
        (req.email,)
    ).fetchone()
    conn.close()

    if not user or user['password_hash'] != hash_password(req.password):
        raise HTTPException(401, 'invalid email or password')

    return {
        'user_id': user['id'],
        'email': user['email'],
        'token': create_token(user['id']),
        'token_balance': user['token_balance'],
    }


@app.get('/api/me')
def me(user: dict = Depends(current_user)):
    return {
        'id': user['id'],
        'email': user['email'],
        'token_balance': user['token_balance'],
        'created_at': user['created_at'],
    }


# === Chat Endpoint ===
@app.post('/api/chat', response_model=ChatResp)
async def chat(req: ChatReq, user: dict = Depends(current_user)):
    if user['token_balance'] <= 0:
        raise HTTPException(402, 'insufficient tokens, please top up')

    # 调 AI
    try:
        result = await call_ai(req.message, req.model)
    except Exception as e:
        raise HTTPException(500, f'AI call failed: {str(e)}')

    tokens_used = result['total_tokens']

    # 检查余额
    if user['token_balance'] < tokens_used:
        # 扣到 0
        tokens_used = user['token_balance']

    new_balance = user['token_balance'] - tokens_used

    # 更新 DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE users SET token_balance = ? WHERE id = ?', (new_balance, user['id']))
    c.execute(
        'INSERT INTO usage (user_id, prompt_tokens, completion_tokens, total_tokens, model, created_at) VALUES (?, ?, ?, ?, ?, ?)',
        (user['id'], result['prompt_tokens'], result['completion_tokens'], tokens_used, USE_PROVIDER, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

    return ChatResp(
        reply=result['reply'],
        tokens_used=tokens_used,
        token_balance=new_balance,
    )


@app.get('/api/usage')
def usage(user: dict = Depends(current_user)):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        'SELECT * FROM usage WHERE user_id = ? ORDER BY created_at DESC LIMIT 50',
        (user['id'],)
    ).fetchall()
    conn.close()

    return {
        'user_id': user['id'],
        'recent_usage': [dict(r) for r in rows]
    }


# === Static frontend (must be last, after all API routes) ===
FRONTEND_DIR = Path(__file__).parent.parent / 'frontend'
if FRONTEND_DIR.exists():
    app.mount('/', StaticFiles(directory=str(FRONTEND_DIR), html=True), name='static')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
