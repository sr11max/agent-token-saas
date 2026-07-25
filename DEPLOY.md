# CheapToken 部署清单

> 给老板的执行步骤。每步标了"我做完了" / "你来做"。
> AI 助手会做不需要 GitHub 凭证的部分。

---

## ✅ 已做完（AI 自动）

- [x] `frontend/index.html` —— 单页 chat，注册/登录/余额/对话
- [x] `backend/main.py` —— 加 StaticFiles mount + 修 deepseek 模型名
- [x] `.gitignore` —— Python/DB/secrets/log
- [x] `Procfile` —— Railway 启动命令
- [x] `railway.toml` —— Railway 部署配置（health check + restart policy）
- [x] `marketing/account_kit.md` —— 养号 3 天计划 + 评论/DM 话术
- [x] `marketing/feedback_survey.md` —— 5 用户反馈表
- [x] E2E 本地测试通过（注册 → chat → 扣 token）

---

## 📋 你要做的（按顺序）

### 步骤 1：告诉我你的 git email + GitHub 用户名

```powershell
git config --global user.email "your@email.com"
git config --global user.name "Your Name"
```

发我邮箱 + GitHub 用户名，我接着 `git init + commit + 准备 push`。

---

### 步骤 2：建 GitHub repo + push（2 个方案二选一）

**方案 A（推荐 · 我能 push）**：
1. 浏览器打开 https://github.com/new
2. 仓库名：`agent-token-saas`
3. 选 **Public**
4. **不要勾** "Add a README" / "Add .gitignore" / "Choose a license"
5. 点 Create
6. 复制 repo URL（形如 `https://github.com/<你的用户名>/agent-token-saas.git`）
7. 把 URL 发我，我自动 push + 完善 README

**方案 B（你 push）**：
1. 同上建 repo
2. 终端跑：
   ```powershell
   cd C:\Users\Administrator\.openclaw\workspace\agent-token-saas
   git init
   git add .
   git commit -m "Initial MVP"
   git branch -M main
   git remote add origin https://github.com/<你的用户名>/agent-token-saas.git
   git push -u origin main
   ```
3. push 时输 GitHub 用户名 + PAT（密码）

---

### 步骤 3：部署 Railway（5 min）

1. 浏览器打开 https://railway.app
2. **GitHub 登录**（用刚建的 GitHub 账号）
3. **New Project** → **Deploy from GitHub repo** → 选 `agent-token-saas`
4. Railway 自动检测 Python，开始构建
5. 等构建完成（1-2 min），点 **Variables** 加：
   - `DEEPSEEK_API_KEY` = `sk-bcb62...`（你现有的）
   - `JWT_SECRET` = （任意 32+ 字符随机串）
   - `AI_PROVIDER` = `deepseek`
   - `DEEPSEEK_MODEL` = `deepseek-v4-flash`
6. 点 **Settings** → **Networking** → **Generate Domain**（拿到 `*.up.railway.app` 子域）
7. 浏览器打开子域，**应该看到 CheapToken 单页**

**Railway 信用卡**：Hobby plan 要 $5 押金（验证后退款），可绑卡或用 GitHub Student Pack。

---

### 步骤 4：加 Volume（持久化 SQLite）

> ⚠️ **不做这步，重启后用户数据全丢**

1. Railway 项目页 → 点 backend service
2. **Settings** → **Volumes** → **New Volume**
3. Mount Path: `/app/data`
4. 加环境变量 `DB_PATH=/app/data/data.db`
5. Redeploy

---

### 步骤 5：注册 Reddit / X 账号（养号启动）

**Reddit**：
1. https://www.reddit.com/register
2. 用户名：`CheapTokenDev`（备选 `CheapTokenAPI`）
3. 邮箱：**别用 QQ 邮箱**（会被当垃圾源）→ 用 Gmail 或 ProtonMail
4. bio 直接抄 `marketing/account_kit.md` 第 2 节

**X (Twitter)**：
1. https://twitter.com/i/flow/signup
2. 用户名：`@cheaptoken_dev`
3. **要手机号** —— TextNow（免费美/加号）/ 5SIM（$1 一次性）
4. bio 同上

---

### 步骤 6：养号 3 天 + 发帖（Day 4）

按 `marketing/account_kit.md` 第 3 节的 Day 1-4 计划走。

**关键**：
- Day 1-3 不发营销内容
- Day 4 美东 9-11 AM EST（北京时间 21-23 点）发 Show HN
- 同一天发 X 推

---

### 步骤 7：找 5 个真用户

按 `marketing/account_kit.md` 第 7 节。

5 个**真名/真邮箱**用户，回 `feedback_survey.md` 5 个问题。

---

## 🚨 卡点预判

| 卡点 | 怎么解决 |
|------|---------|
| Railway 部署报错（环境变量没生效）| 看 Deployments 日志，修后 Redeploy |
| 海外 IP 调 DeepSeek 慢/失败 | 切 `AI_PROVIDER=openrouter` |
| Reddit 账号注册要邮箱验证 | 用 ProtonMail |
| X 注册要手机号 | TextNow 免费 |
| Show HN 帖被删 | 账号 karma 不够 → 再养 1-2 天重发 |

---

## 📊 进度跟踪

每完成一步告诉我，我同步状态。Day 7 目标 = 5 真用户 + 3 反馈 + 1 付费意愿。