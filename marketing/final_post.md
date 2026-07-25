# Reddit/HN 发帖最终版 · 2026-07-25

> 老板风格 + 5 个标题候选 + 可发版本

## 标题（5 选 1）

1. **Show HN: I built a $5/mo AI API from China because Stripe won't let me open an account** ← 推荐
2. Show HN: A token-metered AI service for developers who can't use Stripe
3. Show HN: I'm building cheap AI infra for non-US developers, day 1
4. Show HN: How I built a $5/mo AI SaaS from China with $0 budget
5. Show HN: A real, working AI API for indie devs tired of OpenAI pricing

---

## 正文（推荐 #1 标题版）

```
Hi HN,

I'm a solo developer from China. Two months ago I was laid off and
started building a cheap AI API for indie devs tired of $20/mo OpenAI
subscriptions and the Stripe barrier.

This is day 1 of public building. MVP is done, runs locally, costs me $0
to run right now. Not selling anything yet — just want feedback before
I burn money on ads.

What I built:

- FastAPI backend, Next.js 14 frontend, runs on Vercel free tier
- Token-metered access, JWT auth, no SDK needed (just HTTP)
- AI routed through OpenRouter (one key = 100+ models)
- Free tier: 50K tokens one-time (no credit card)

Pricing:

- Free: 50K one-time tokens
- $5/mo: 500K tokens (~3000 simple chat)
- $19/mo: 3M tokens (personal heavy use)
- $99/mo: 20M tokens (small team)

Why this exists (the real pain I had):

1. I'm a developer in China. I literally cannot open a Stripe account.
   No overseas entity, no US bank, no nothing.
2. OpenAI charges $3-20/M tokens. DeepSeek charges $0.27/M. The math
   doesn't add up — somebody's pocketing the difference.
3. PayPal works but withdrawals are a 7-day nightmare with a 5% haircut.
4. Most "cheap AI API" alternatives I tried either died, had hidden
   rate limits, or required me to send 5 emails to get a key.

What I learned (so far):

1. Token accounting is harder than calling the AI. Race conditions,
   partial responses, refunds, edge cases — it adds up to real code.
2. OpenRouter is the killer feature. 1 key = 100+ models. I haven't
   written a single model-specific adapter.
3. Building is 30% of the work. Marketing is 70%. The code is the
   easy part.
4. Free tier is non-negotiable. Nobody signs up for an untested API.
5. Cross-border ops is the biggest moat for Chinese devs. Stripe
   alone blocks 90% of would-be founders.

What I want feedback on:

- Is $5 the right entry point for indie devs?
- Naming: working title is "CheapToken" but I'm open to suggestions
- What core feature would make you actually switch from OpenAI?

30-day goal: 100 active users, $500 MRR. I'll post updates here with
real numbers (not vanity metrics).

Currently working on:
- Public deployment (Vercel + Railway)
- Landing page
- First 5 beta testers (friends, no real users yet)

Ask me anything about:
- Why I chose FastAPI over Django
- How I handle token refunds when the API fails mid-response
- The China → overseas SaaS path
- The 7-day OpenRouter vs direct DeepSeek comparison

No product link yet — DM me for early access if you want to poke
around. I'm not selling anything; I just want to know if this is
worth finishing.
```

---

## X 短推（3 条）

### 推 1（Day 1）
```
Day 1 of building a $5/mo AI API from China.

Stack: FastAPI + Next.js + OpenRouter.
Cost so far: $0.
Status: MVP, runs locally, not deployed yet.

Not selling anything. Just want feedback before I burn money.

#buildinpublic
```

### 推 2（Day 2-3）
```
Day 2 update:

Backend: ✅ auth + chat + token accounting
Frontend: 🚧 in progress
Marketing: 1 Reddit post drafted, 2 X threads queued

Token accounting is harder than calling the AI. Race conditions, partial
failures, refunds — it adds up to real code.
```

### 推 3（Day 3-4）
```
Day 3 update:

First 5 beta testers lined up (all friends, no real users).

The hardest part isn't building. It's not being embarrassed to post
"hey I made a thing" in public.

Will publish the Reddit post tomorrow at 9am EST.
```

---

## Medium 博客（1500 字）

### 标题（3 选 1）
1. **Why I'm Building a $5/mo AI API From China (And Why Stripe Is the Real Problem)**
2. I Lost My Job and Started a SaaS: 30 Days In
3. The Real Cost of Building Cheap AI From a Country Where Stripe Doesn't Work

### 大纲

#### Part 1: The Setup (300 字)
- 2 个月前被裁
- 看着 OpenAI / Anthropic 的定价生气
- 算了一笔账：DeepSeek V3 = $0.27/M，OpenAI GPT-4o-mini = $0.15/M，**实际成本** vs **实际收费**
- 中国独立开发者的处境：没 Stripe、没海外公司、PayPal 提现 7 天 + 5%

#### Part 2: The Stack (400 字)
- FastAPI 不是 Django（异步、文档好、AI 生态好）
- Next.js 14 不是 Vue（Vercel 原生、SEO 不用折腾）
- OpenRouter 不是直连（1 个 key = 100+ 模型 = 1 行代码切模型）
- Vercel 不是自建（早期 0 运维成本）

#### Part 3: The Real Challenges (400 字)
- **Token accounting**（不是调 AI，是计量）
- **Marketing > Coding**（70% 时间在找用户）
- **Cross-border ops**（Stripe / PayPal / 提现 / 汇率）
- **Free tier 设计**（50K tokens 不多不少，刚好测 50 次）

#### Part 4: The 30-Day Plan (200 字)
- 第 1 周：MVP + Landing Page
- 第 2 周：Reddit / X 营销
- 第 3 周：Product Hunt + HN
- 第 4 周：评估 + 转方向

#### Part 5: What I Don't Know (200 字)
- $5 定价对吗？
- "CheapToken" 名字对吗？
- 海外用户愿不愿意付钱给中国人？
- 哪天 Stripe 解禁中国？不知道

---

## 老板接下来做的

1. **选 1 个标题**（我推荐 #1）
2. **告诉我改哪里**（基于你这版的微调）
3. **准备好 2 个链接占位符**：
   - product link（或者改成 "DM me for access"）
   - X/Twitter link（你的账号）

---

## 我接下来做的

- 写 Next.js 前端最小版
- 写 landing page
- 写 GitHub README（作为 fallback 链接）
- 写 product link（哪怕是简单 README）

**老板，**你拍板。**