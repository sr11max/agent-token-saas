# 养号 / 账号启动包

> 适用平台：Reddit + X (Twitter)
> 时间窗：Day 1-3 养号 → Day 3-4 发帖
> 准备：账号名、bio、首批评论话术、DM 模板、反馈收集

---

## 1. 账号名（双平台统一品牌）

| 平台 | 用户名 | URL |
|------|--------|-----|
| Reddit | `CheapTokenDev` | reddit.com/u/CheapTokenDev |
| X | `@cheaptoken_dev` | x.com/cheaptoken_dev |
| GitHub | `agent-token-saas` | github.com/<your-username>/agent-token-saas |

**备用名**（如果主名被占）：
- Reddit: `CheapTokenAPI`, `cheaptoken-build`
- X: `CheapTokenAPI`, `buildcheaptoken`

---

## 2. Bio 文案（直接抄）

### Reddit bio
```
Solo dev from China. Building CheapToken - cheap AI API for indie devs
who can't use Stripe. $0 to start, $5/mo to scale. Day 1 building in public.
Posts about API design + token economics.
```

### X bio
```
Building CheapToken 🇨🇳
Cheap AI API for indie devs ($5/mo, no Stripe)
$0 → $5/mo · solo dev · build in public
```

---

## 3. 养号 3 天计划（不间断）

### Day 1（注册当天）
- [ ] 注册 Reddit 账号（要邮箱，建议 ProtonMail / Gmail 别用 QQ）
- [ ] 注册 X 账号（**要手机号** — 用国外手机号或 eSIM 服务如 TextNow）
- [ ] 验证邮箱
- [ ] 上传头像（AI 生成或纯色）
- [ ] 写 bio（直接抄上面）
- [ ] **不！发！任！何！营！销！内！容！**

### Day 2（攒 karma）
- [ ] 进 5 个 subreddit：`r/SideProject` / `r/IndieHackers` / `r/InternetIsBeautiful` / `r/LocalLLaMA` / `r/ChatGPT`
- [ ] 给每个 subreddit 的置顶/Welcome 帖点赞
- [ ] 找 3-5 个**最近 24h 的 high-quality 帖**，留下**真诚评论**（用话术 A/B）
- [ ] X 上 follow 5-10 个 indie dev 大佬（@levelsio, @marc_louvion, @csaborzi 等）
- [ ] 发 2-3 条**非营销推**（生活、思考、技术笔记）

### Day 3（建立存在）
- [ ] Reddit：再评论 5-10 个帖子，目标 karma ≥ 50
- [ ] X：发 1-2 条 #buildinpublic 推（**不卖产品**，只讲进度）
- [ ] 草拟 Show HN 帖（用 `final_post.md`）
- [ ] **Day 3 结束前不发主帖**

### Day 4（发布）
- **美东时间 9-11 AM EST**（北京时间 21-23 点）发 Show HN
- 同一天 X 发 3 条推（用 `day1_reddit.md` 里那 3 条）
- DM 10 个目标 indie devs

---

## 4. 评论话术（3 类，按场景用）

### A. 真诚兴趣型（看到"Just launched X"类帖子）
```
Curious - did you bootstrap it from day 1 or did you have funding?
I'm working on a similar side project (API side of things) and
trying to figure out the right pace.
```

### B. 经验分享型（看到"How do you monetize" / 痛点讨论）
```
Hit the same wall. For me the breakthrough was switching from
monthly subscription to credit-based pricing - users hated
"another $20/mo subscription" but were fine with $5 one-time
top-ups. Might be worth a try.
```

### C. 求建议型（看到"How I built X"技术帖）
```
How are you handling [specific thing]? I'm at the same stage
and still figuring it out. Did you roll your own or use [library]?
```

---

## 5. DM 模板（给目标 indie devs）

### 邀请测试型（短）
```
Hey! Saw your post about [X] - I'm building a cheap AI API
side project (token-metered, $5/mo, for indie devs who can't
use Stripe). If you ever want to swap notes or test each
other's stuff, let me know. https://cheaptoken.up.railway.app
```

### 求反馈型（中等长度）
```
Hey [name] - I'm a solo dev building CheapToken, a $5/mo
AI API for indie devs. MVP just shipped (FastAPI + OpenRouter).

Would love 5 min of feedback if you have time. I won't email
you or try to sell anything - just want to know if this is
worth finishing.

Link: https://cheaptoken.up.railway.app

Either way, keep shipping.
```

---

## 6. 反馈收集表（5 个真用户填这个）

发完 DM 后，让每个用户回这 5 个问题：

```
1. 怎么发现我们的？（Reddit / X / 朋友 / 其他）
2. 注册流程跑通了吗？（Y / N —— N 的话哪里断了）
3. 实际用了 chat 吗？（Y / N —— N 的话为什么）
4. 最想改的 1 件事是？
5. 会付 $5/月吗？（Y / N —— N 的话为什么不）
```

**关键**：不是"问用户会不会用" —— **5 个回答足够识别明显问题**（如流程断在第 3 步）。

---

## 7. 5 个真用户从哪里找

| 渠道 | 难度 | 时间 | 期望转化 |
|------|------|------|---------|
| 朋友圈 / 校友群 | 低 | 10 min | 2-3 个测试 |
| V2EX / 即刻 发帖 | 中 | 30 min | 2-3 个陌生人 |
| DM 10 个 Reddit 活跃用户 | 中 | 30 min | 1-2 个回复 |
| 微博 / 豆瓣 AI 小组 | 低 | 20 min | 1-2 个 |

**Day 4-5 内找齐 5 个**，每个**真名/真邮箱**的（不要 test_xxx 自动测试）。

---

## 8. 风险清单

- ⚠️ Reddit 新账号发链接 = 90% 进 spam → 严格养号 2-3 天
- ⚠️ X 新账号发链接限流 → 先发推互动建可信度
- ⚠️ 海外手机号获取：TextNow（免费美/加号）、5SIM（$1 一次性）、或借朋友的
- ⚠️ 邮箱别用 QQ 邮箱（容易被 Reddit/X 当垃圾源） → ProtonMail 或 Gmail