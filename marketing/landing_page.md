# Landing Page 文案（草稿）· 2026-07-25

> 用老板风格 + 独立开发者调子

---

## Hero 区块

### 标题（3 选 1）

1. **AI API that doesn't need a US bank account** ← 推荐
2. Cheap AI tokens for indie devs (no Stripe, no hassle)
3. Token-metered AI, $5/month, works from anywhere

### 副标题

> FastAPI + OpenRouter. Free 50K tokens. No credit card.

### CTA 按钮

- 主按钮：**Get 50K free tokens**
- 次按钮：**See the code**（指向 GitHub）

---

## 痛点区块

### 3 个具体痛点

1. **Stripe blocks non-US developers.** No way to pay even if you want to.
2. **OpenAI charges $20/mo minimum.** For what? 1M tokens you'll never use.
3. **Most "cheap AI" alternatives have hidden rate limits.** You find out after you sign up.

---

## 方案区块

### 4 个真实卖点

1. **Free tier is real.** 50K tokens, no credit card, no email verification beyond signup.
2. **$5/mo gets you 500K tokens.** That's ~3000 simple chat. Real money's worth.
3. **OpenRouter under the hood.** 1 key = 100+ models. Switch between DeepSeek, Llama, Claude, GPT without code changes.
4. **Token accounting you can audit.** Every request, every refund, every rate limit — visible.

---

## 对比表

| | OpenAI | Other "cheap" APIs | This |
|---|---|---|---|
| Free tier | $0 (limited) | "Free trial" (credit card required) | **50K tokens, no card** |
| $5/mo gets you | 0 | 100K (with limits) | **500K tokens** |
| Multiple models | Pay per model | One model only | **100+ via OpenRouter** |
| Sign up friction | High | Medium | **Email + password only** |
| Works from China | ❌ | ⚠️ | ✅ |
| Token refunds on error | Manual | Never | **Automatic** |

---

## 技术栈透明区

```
Backend:    FastAPI + SQLite (dev) → Postgres (prod)
Frontend:   Next.js 14 (App Router)
AI:         OpenRouter (DeepSeek / Llama / Claude / GPT)
Auth:       JWT (Clerk planned)
Deploy:     Vercel + Railway
```

**Why these choices** (3 句话):
- FastAPI because async, good docs, AI ecosystem
- OpenRouter because 1 key = 100+ models, no vendor lock-in
- Vercel because early-stage projects shouldn't pay for servers

---

## 公开路线图

### ✅ Done
- MVP backend (auth + chat + token accounting)
- Free tier (50K tokens)
- 5 beta testers running

### 🚧 This week
- Landing page (you are here)
- Public Reddit post
- X build-in-public thread

### 📅 Next 30 days
- ProductHunt launch
- HackerNews Show HN
- 100 users / $500 MRR target

### 🔮 Beyond
- Multi-language support
- Team billing
- Custom model fine-tuning

---

## FAQ（5 个真问题）

**Q: Is this legal?**
A: Yes. You're paying for API access. We're not selling tokens as securities.

**Q: Can I get a refund?**
A: No refunds on subscription. Free tier exists for testing.

**Q: What happens to my data?**
A: We don't store your prompts or responses. Only metadata (timestamps, token counts).

**Q: Why $5? Why not $1?**
A: $1 doesn't pay for support. $5 keeps us motivated and you under budget.

**Q: When will Stripe work?**
A: Unknown. We built this so we don't have to wait.

---

## CTA 末段

> **Try it now: 50K free tokens, no credit card.**
> Built by 1 person in China. $0 to start. $5/mo to keep going.
> 
> [Get started] · [Read the code] · [Follow the journey]

---

## 副文（footer）

*Status: MVP, 100% local tested. No third-party tracking. No ads. No email list. Just a working tool.*

*Source: [github] · Built by [@cheaptoken]*
