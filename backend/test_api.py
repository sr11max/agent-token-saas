#!/usr/bin/env python3
"""
测试 API 是否能跑通
"""
import requests
import time

BASE = 'http://127.0.0.1:8000'

print('=== 1. Health check ===')
r = requests.get(f'{BASE}/health')
print(f'  Status: {r.status_code}, Body: {r.json()}')

print('\n=== 2. Register ===')
email = f'test_{int(time.time())}@qq.com'
password = 'test123456'
r = requests.post(f'{BASE}/api/auth/register', json={'email': email, 'password': password})
print(f'  Status: {r.status_code}, Body: {r.json()}')

if r.status_code != 200:
    print('Register failed, abort')
    exit(1)

token = r.json()['token']
headers = {'Authorization': f'Bearer {token}'}

print('\n=== 3. Login ===')
r = requests.post(f'{BASE}/api/auth/login', json={'email': email, 'password': password})
print(f'  Status: {r.status_code}, Body: {r.json()}')

print('\n=== 4. Get me ===')
r = requests.get(f'{BASE}/api/me', headers=headers)
print(f'  Status: {r.status_code}, Body: {r.json()}')

print('\n=== 5. Chat ===')
r = requests.post(f'{BASE}/api/chat', json={'message': '你好，1+1=?'}, headers=headers)
print(f'  Status: {r.status_code}, Body: {r.json()}')

print('\n=== 6. Usage ===')
r = requests.get(f'{BASE}/api/usage', headers=headers)
print(f'  Status: {r.status_code}, Body: {r.json()}')

print('\n✅ All tests passed')
