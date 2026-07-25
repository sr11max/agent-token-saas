# Automation Scripts

> 用 Playwright + stealth 做的浏览器自动化脚本
> 学习产出：token-saas 找 5 个真用户 + 端到端测试

---

## 1. `e2e_test.py` — token-saas 端到端测试

**用途**：自动化测试整个 token-saas 流程（注册 → 调 AI → 扣费 → 验证）

**前置**：
- token-saas 已部署到 Railway
- 你有 Railway 分配的 URL（形如 `https://xxx.up.railway.app`）

**用法**：

```bash
cd agent-token-saas
python scripts/e2e_test.py --url https://YOUR-RAILWAY-URL.up.railway.app
```

**测什么**：
- [1] `GET /` 主页能加载
- [2] `POST /api/auth/register` 注册成功
- [3] `POST /api/chat` 调 AI 成功
- [4] token 扣费正确（50000 → 49872 → ...）
- [5] `GET /api/me` 余额正确
- [6] UI 流程（注册表单 → chat 面板）
- [7] `GET /health` 健康检查

**截图**：`e2e-1-home.png` / `e2e-6-ui.png`

**什么时候跑**：
- 每次 Railway 部署后（确保没回归）
- 用户反馈 bug 时（快速定位）

---

## 2. `reddit_showhn.py` — Reddit 自动化

**用途**：自动养号 + 发 Show HN 帖

**前置**：
- Reddit 账号
- ⚠️ Reddit **不欢迎自动化**（账号风险）—— **用小号 / 二手账号**

**用法**：

```bash
# 1. 填账号（编辑 CONFIG dict）
# 改 reddit_showhn.py 里的 CONFIG["reddit"]["username"] 和 ["password"]

# 2. 跑
python scripts/reddit_showhn.py --action login
python scripts/reddit_showhn.py --action browse --subreddit SideProject --minutes 5
python scripts/reddit_showhn.py --action post

# 一次跑完（login + browse + post）
python scripts/reddit_showhn.py --action all

# 用 headed 模式看（首次调试用）
python scripts/reddit_showhn.py --action login --no-headless
```

**做什么**：
- **login**：登录 Reddit 账号
- **browse**：浏览 subreddit（5 分钟）+ 随机 upvote + scroll + next page + click post
- **post**：自动填 Show HN 帖（从 `marketing/final_post.md` 读）+ **截图让你审核**（不自动 submit）
- **all**：login → browse → post

**行为模拟**：
- 随机延迟 3-15 秒（不像 bot）
- 不规律点击（用 weighted random）
- stealth：navigator.webdriver 改写 + 真实 user-agent
- 不自动 submit（最后一步人工审核）

**养号策略**：
- Day 1-2：每天 browse 3-5 个 subreddit，每次 5-10 分钟
- Day 3-4：开始发内容（评论为主，post 谨慎）
- Day 4-5：发 Show HN 主帖

---

## 3. `probe_railway_urls.py` — Railway URL 探测

**用途**：找不到 Railway 分配的 URL 时扫一遍

```bash
python scripts/probe_railway_urls.py
```

**扫的 URL**：
- cheaptoken.up.railway.app
- agent-token-saas.up.railway.app
- sr11max.up.railway.app
- 等等（可以加）

---

## 依赖

```bash
pip install playwright psutil
playwright install chromium
```

Chrome / chrome-headless-shell 已被 Playwright 自带（不需要装系统 Chrome）。

---

## 风险 / 合规

⚠️ **Reddit 自动化违反 Reddit ToS**：
- 账号可能被 ban
- 不要在主账号上跑
- 每天操作不要太密集（< 30 min/天）

⚠️ **E2E 测试 + 自动化运维** 没问题（自家产品）

---

## 输出

跑完 E2E 测试：
- `e2e-1-home.png`（主页截图）
- `e2e-6-ui.png`（UI 流程截图）
- terminal log（每个步骤 ok/fail）

跑完 Reddit post：
- `reddit_post_<timestamp>.png`（发帖前截图，**人工审核**）
- terminal log（每个步骤）

---

## 实战时间线建议

| Day | 任务 | 脚本 |
|-----|------|------|
| Day 1 | token-saas 部署 + E2E 验证 | `e2e_test.py` |
| Day 2-3 | 准备 Reddit 账号 + 填 CONFIG | — |
| Day 3-5 | 每天 1 次 `browse` 5-10 min | `reddit_showhn.py` |
| Day 5 | 发 Show HN 帖 | `reddit_showhn.py --action post` |

**5 天后**：账号有 karma，Show HN 帖上线，开始有真实流量。