# Reddit 发帖草稿 · 2026-07-25

> 目标：r/SideProject 或 r/InternetIsBeautiful
> 目的：种子用户 + 早期反馈

---

## 标题（5 选 1）

1. **Show HN: I built a cheap AI agent API from China (no Stripe, no overseas entity)**
2. Show HN: Building a $5/mo AI SaaS from China with $0 budget
3. Show HN: I made a cheap AI wrapper because OpenAI is too expensive
4. Show HN: My 30-day challenge building an AI SaaS with no money
5. Show HN: How I built a token-metered AI service from scratch

---

## 正文（推荐 #1）

```
Hi HN,

I'm building a cheap AI agent service for developers who don't want to pay
$20/mo for OpenAI or deal with credit cards.

Stack: FastAPI + Next.js + DeepSeek (via OpenRouter) + Postgres + Vercel
Status: MVP, $0 spent, runs locally

Why this exists:
- I lost my job 2 months ago and needed a side project
- I noticed OpenAI/Anthropic charge $3-20/M tokens but the actual cost is $0.10-0.50
- I want to build a "AI for the rest of us" - simple, cheap, no friction

The product:
- Free: 50K tokens (one-time)
- $5/mo: 500K tokens (~3000 simple chat)
- $19/mo: 3M tokens
- $99/mo: 20M tokens (small team)

Stack details:
- Backend: FastAPI + SQLite (dev) → Postgres (prod)
- Frontend: Next.js 14 (app router)
- Auth: JWT (Clerk later)
- AI: OpenRouter (1 key, multiple models, deepseek/llama/claude/gpt)
- Deploy: Vercel (free tier)

Things I learned so far:
1. OpenRouter is the killer feature - 1 key = 100+ models
2. Token accounting is harder than I thought
3. Marketing > coding (no one finds your product by accident)
4. Free tier is essential - nobody signs up without trying
5. Stripe is a pain for non-US developers (need overseas entity)

What I want feedback on:
- Pricing - is $5 the right entry point?
- Naming - I'm calling it "CheapToken" right now (placeholder)
- Features - what would make you switch from OpenAI?

Next 30 days: get to 100 users and $500/mo MRR. Will post updates here.

If you want to try it: [link]
If you want to follow along: [@cheaptoken on X]

Happy to answer any questions about the technical side, the China-to-overseas
market, or the "build a SaaS with $0" experience.
```

---

## 标题变体

如果想在 r/ChatGPT 发（更通用）：

> **I built a $5/mo ChatGPT alternative from China with DeepSeek under the hood**

如果想在 r/LocalLLaMA 发（技术向）：

> **Show HN: Token-metered AI API with model routing (DeepSeek + Llama + Claude)**

---

## 配套 X 短推（3 条）

### 推 1（Day 1）
```
Day 1 of building an AI SaaS from China 🇨🇳

Cost so far: $0
Stack: FastAPI + Next.js + OpenRouter
Goal: 100 users in 30 days

No Stripe yet. No marketing budget. Just code and Reddit.

#buildinpublic
```

### 推 2（Day 2）
```
Day 2 update:
- Backend: ✅ works (auth + chat + token accounting)
- Frontend: 🚧 in progress
- Marketing: prepping Reddit post for tomorrow

The interesting part: token accounting is harder than calling the AI.
You need to handle race conditions, partial failures, refunds, etc.
```

### 推 3（Day 3）
```
Day 3 update:
- Reddit post drafted (Show HN)
- Will post at 9am EST tomorrow
- First 5 testers lined up (friends, no real users yet)

The hardest part isn't building. It's not being embarrassed to post.
```

---

## 配套 Medium 博客（1500 字）

**标题**：
> Why I'm Building a Cheap AI SaaS From China (And the Real Challenges Nobody Talks About)

**大纲**：

### Part 1: The Story
- 个人背景（失业 + 副业尝试）
- 为什么选 SaaS 不是加密货币
- 为什么选 AI 不是内容

### Part 2: The Stack
- 为什么 FastAPI 不是 Django
- 为什么 Next.js 不是 Vue
- 为什么 OpenRouter 不是 OpenAI 直连
- 为什么 Vercel 不是自建

### Part 3: The 3 Real Challenges
1. **收款** - Stripe 要海外身份，PayPal 提现麻烦
2. **营销** - 国内做内容、海外用户找
3. **价格战** - OpenAI 自己都便宜，我有什么差异化

### Part 4: The Plan
- 30 天目标
- 90 天目标
- 退出机制（什么时候承认失败）

### Part 5: Open Questions
- $5 定价对吗？
- 哪些场景值得做？
- 怎么不被 GPT-4o 取代？

---

## 老板接下来要做的事

### 今晚
1. **review 这 3 篇草稿**
2. 改 3-5 处个人细节（你的真实经历、你的代码报错）
3. 我重写

### 明天
1. 注册 Reddit / X 账号
2. 等 1-2 天养号（先浏览、互动）
3. 第 3 天发第一篇

---

## 我接下来要做的事（今晚）

1. 写 Next.js 前端最小版
2. 写部署脚本
3. 录一个 5 分钟 demo 视频脚本

**老板，**review 完帖子后我接着干。**