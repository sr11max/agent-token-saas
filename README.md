# agent-token-saas

> Cheap AI tokens for indie devs who can't use Stripe

A solo project. 1 developer. $0 to start. MVP done.

## 实际是什么

- 一个 **token-metered AI API**（按调用量收费）
- 后端：**FastAPI**
- 前端：**单页 HTML**（未来切 Next.js）
- AI 调度：**OpenRouter**（1 key = 100+ 模型）
- 数据库：开发用 **SQLite**，生产用 **Postgres**
- 认证：**JWT**（后续 Clerk）
- 部署：**Vercel** + **Railway**

## 我为什么做这个

我是中国的独立开发者。OpenAI 一个月 $20 起步——用不上。Stripe 不要我（要海外身份）。

我算了一笔账：
- DeepSeek V3 API：**$0.27 / 1M tokens**（实际成本）
- OpenAI GPT-4o-mini：**$0.15 / 1M input**
- 卖给独立开发者的"cheap AI"：**$3-20 / 1M**

中间的钱被谁赚了？**不是 AI 本身。**

所以我做了这个。

## 实际跑起来什么样

| 套餐 | 价格 | 包含 |
|------|------|------|
| Free | $0 | 50K tokens（一次性，够测 50 次）|
| Starter | $5/月 | 500K tokens |
| Pro | $19/月 | 3M tokens |
| Team | $99/月 | 20M tokens |

## 怎么跑起来

### 1. 装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 2. 配环境变量

```bash
# 必须（开发）
export DEEPSEEK_API_KEY=***

# 可选（生产）
export OPENROUTER_API_KEY=***
export AI_PROVIDER=openrouter
export JWT_SECRET=***
```

### 3. 启动

```bash
cd backend
python main.py
```

或者：

```bash
uvicorn main:app --reload --port 8000
```

### 4. 测

```bash
cd backend
python test_api.py
```

## API 端点

| 端点 | 方法 | 说明 |
|------|------|------|
| `/health` | GET | 健康检查 |
| `/api/auth/register` | POST | 注册（送 50K tokens）|
| `/api/auth/login` | POST | 登录 |
| `/api/me` | GET | 我的信息 |
| `/api/chat` | POST | 调 AI（扣 token）|
| `/api/usage` | GET | 用量 |

API 文档：http://127.0.0.1:8000/docs

## 我学到的（30 天项目笔记）

1. **Token accounting 比调 AI 难。** Race conditions、partial failures、refund 校准——这些是核心代码。
2. **OpenRouter 是最大的效率提升。** 1 个 key = 100+ 模型，省了 5 倍的接入工作。
3. **写代码 30%，找用户 70%。** 代码容易，找用户难。
4. **Free tier 不可省。** 没人会为一个没测过的 API 付钱。
5. **跨境运营是中国独立开发者的最大门槛。** 单 Stripe 一项就挡住了 90% 想做 SaaS 的人。

## 路线图

- [x] MVP（注册 / 登录 / 调 AI / 扣费）
- [x] 跑通 DeepSeek + OpenRouter
- [x] 单页 HTML 前端
- [x] 部署到 Railway
- [ ] 营销（Reddit / X / Show HN）
- [ ] 5 个真实测试用户 + 反馈
- [ ] ProductHunt + Medium 发布
- [ ] 100 用户 / $500 MRR

## 状态

- 状态：MVP + 单页前端，**已部署 Railway**
- 预算：**$0 启动**（开发用 DeepSeek key）
- 下一里程碑：Show HN + 5 个真实测试用户

## 我是谁

1 个独立开发者。中国。被裁 2 个月。靠 $0 启动资金做这个。

*不卖任何东西——产品是副业，文章是日记。*

---

**License:** MIT
**Code:** [github.com/sr11max/agent-token-saas](https://github.com/sr11max/agent-token-saas)
**Live:** https://cheaptoken.up.railway.app（部署后填入）
**Status:** Day 1, building in public
