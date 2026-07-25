# 5 用户 DM 模板（直接发）

> 给 Reddit / V2EX / 独立开发者群 / 即刻 / 微博 等渠道的目标用户
> **不要群发**（被识别为 spam 必封号），**每个目标用户单独定制**（参考对方项目）

---

## 模板 1：Reddit DM（给 r/SideProject / r/IndieHackers 活跃用户）

> **前置**：在 r/SideProject / r/IndieHackers 找 10 个**最近 7 天发过帖**的人，看他们的项目。
> **定制**：第一句必须提到对方的具体项目。

```
Hey [name],

Just saw your [project name] on r/SideProject — [一句话点评，比如"the chrome-extension idea is solid"].

I'm building CheapToken, a $5/mo AI API for indie devs who can't use Stripe
(I'm based in China, similar problem). Currently looking for 5 beta testers
to stress-test it before launching publicly.

If you have 5 min this week, would love to know:
- Does [their use case] ever need cheap AI inference?
- What's your biggest pain with OpenAI/Anthropic pricing?

Not pitching anything — just looking for honest feedback from devs
who get the Stripe-problem space.

[Your Reddit username]
https://cheaptoken.up.railway.app
```

**为什么这样写**：
- ✅ 第一句证明你**真的看了对方项目**（不是群发）
- ✅ 简短（5 句话）
- ✅ 明确"5 beta testers" 给出有限性
- ✅ "not pitching anything" 建立非销售语气
- ✅ 留 2 个 open-ended question（容易回复）

---

## 模板 2：X / Twitter DM（给 indie dev 大佬）

> **前置**：在 X 找 #buildinpublic / indie hackers
> **字符限制**：X DM 限制 10000 字符

```
Hey [handle],

Saw you're shipping [project] — the [specific feature] looks great.

I'm building CheapToken, a $5/mo AI API for devs who can't use Stripe
(I'm in China, Stripe blocks us). MVP is live, looking for 5 beta testers.

Worth 5 min to try? Would love your take on whether the pricing/API
actually fits your workflow.

(If not a fit, no worries — your [their project] looks great regardless)

[link]
```

---

## 模板 3：V2EX 发帖（公开帖，不 DM）

> 发到 `/t/promo` 节点

```
标题：[CheapToken] $5/月 AI API，给用不了 Stripe 的独立开发者

正文：
做了个 $5/月的 AI API（按 token 收费），解决国内独立开发者用不了 Stripe 的痛点。

技术栈：
- FastAPI + OpenRouter（1 个 key 切换 100+ 模型）
- DeepSeek V3 / GPT-4o-mini / Llama 都行
- 50K tokens 免费试用（不绑卡）

为什么做这个：
- OpenAI $20/月起步 + Stripe 拒开账户 = 国内独立开发者起步成本爆炸
- 实际推理成本只占 OpenAI 收费的 5-10%
- 想做"AI for the rest of us"

免费试用：[link]

5 个 beta 测试名额，求反馈（5 分钟即可）：
1. 注册 → 拿 50K tokens
2. 调一次 chat → 看余额减少
3. 跑你们自己的 prompt → 反馈速度/质量

不卖任何东西——产品是副业，文章是日记。
GitHub: github.com/sr11max/agent-token-saas
```

---

## 模板 4：即刻 / 豆瓣 AI 小组（中文社区）

```
做了个 $5/月的 AI API：https://cheaptoken.up.railway.app

解决痛点：国内独立开发者用不了 Stripe + OpenAI 太贵

50K tokens 免费试用，不绑卡。

模型走 OpenRouter，可选 DeepSeek V3 / GPT-4o-mini / Llama。

求 5 个 beta 测试者（5 分钟）：注册 + 调一次 chat + 反馈。

技术栈：FastAPI + Next.js + PostgreSQL/Vercel Postgres
```

---

## 模板 5：邮件（给 GitHub 上独立开发者 / Indie Hackers）

> 主题：Feedback wanted: $5/mo AI API for devs who can't use Stripe

```
Subject: Feedback wanted: $5/mo AI API for devs who can't use Stripe

Hi [name],

I noticed your project [project name] on GitHub — [一句话真实反馈，比如"the way you handle X is interesting"].

I'm shipping CheapToken (github.com/sr11max/agent-token-saas), a $5/mo
AI API for indie devs who can't use Stripe. I'm in China, so I get
the Stripe-problem space first-hand.

Currently looking for 5 beta testers to validate the API before
public launch. If you have 5 min this week, would love your take:

- Does [project] need cheap AI inference?
- What's your current workaround for the Stripe issue?
- What would make you switch from your current provider?

Honest feedback only — not pitching anything. If it's not a fit,
honest "no" is more useful than ghosting me.

[live URL]
[GitHub: github.com/sr11max/agent-token-saas]
```

---

## 关键原则

1. **第一句必定制**（"我看了你的项目"——不是群发）
2. **不给大段推销**（最多 5 句话）
3. **明确"5 beta testers"**（不是"百万用户"——有限性 = 可信）
4. **"not pitching" + "honest feedback only"**（建立非销售关系）
5. **问开放问题**（不是 "do you want to buy"——而是 "what's your pain"）
6. **留退路**（"if not a fit, no worries"）

---

## 发送节奏（防 spam）

| Day | 数量 | 渠道 |
|-----|------|------|
| Day 1 | 5 DM | Reddit (1 个 subreddit) |
| Day 2 | 5 DM | X / Twitter |
| Day 3 | 5 DM | V2EX / 即刻 |
| Day 4 | 1 公开帖 | Show HN（用 reddit_showhn.py） |
| Day 5 | 1 公开帖 | V2EX / 即刻 |
| Day 6-7 | 回应回复 | 主动 follow up |

**总**：约 15 DM + 2 公开帖，**期望 5 个真用户回复**（30% 转化）

---

## 不要做

- ❌ 同一天 10+ DM（立刻封号）
- ❌ 群发相同文字（每个目标用户必须定制第一句）
- ❌ 在 DM 里推销售（先建立关系）
- ❌ 假承诺（"免费" 必须真免费）
- ❌ 跟错人（只发给独立开发者，不要发给 enterprise）
- ❌ 重复发（同一个人最多发 1 次）