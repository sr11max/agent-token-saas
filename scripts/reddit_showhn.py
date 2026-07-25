"""
Reddit 自动化脚本
1. 登录 Reddit 账号（用户提供 credential）
2. 自动养号：浏览 r/SideProject / r/IndieHackers / r/LocalLLaMA + 评论
3. 自动发 Show HN 帖（草稿已写好，在 marketing/final_post.md）
4. 自动发 X 推文

⚠️ 使用前用户必须：
- 提供 Reddit 账号
- 提供 X 账号
- 知道 Reddit/X ToS 风险
"""
import argparse
import asyncio
import time
import random
import json
import sys
from pathlib import Path
from playwright.async_api import async_playwright

# 配置文件：用户填入
CONFIG = {
    "reddit": {
        "username": "FILL_IN",   # ← 填 Reddit 用户名
        "password": "FILL_IN",   # ← 填 Reddit 密码
    },
    "x": {
        "username": "FILL_IN",   # ← 填 X 用户名
        "password": "FILL_IN",
    },
    "show_hn_draft": {
        # 从 agent-token-saas/marketing/final_post.md 读
        "title": "Show HN: I built a $5/mo AI API from China (no Stripe, no overseas entity)",
        "subreddit": "SideProject",
        "body_path": "../marketing/final_post.md",
    },
    "behavior": {
        # 模拟人类行为：随机延迟 + 不规律点击
        "min_delay_sec": 3,
        "max_delay_sec": 15,
        "browse_minutes": 5,  # 每次养号时长
    }
}


class RedditAutomation:
    def __init__(self, config):
        self.config = config
        self.context = None
        self.page = None

    async def human_delay(self, min_s=None, max_s=None):
        min_s = min_s or self.config["behavior"]["min_delay_sec"]
        max_s = max_s or self.config["behavior"]["max_delay_sec"]
        delay = random.uniform(min_s, max_s)
        print(f"  [delay] {delay:.1f}s")
        await asyncio.sleep(delay)

    async def launch(self, headless=True):
        """启 chromium + stealth"""
        from playwright.async_api import async_playwright
        self._playwright = await async_playwright().start()
        self.browser = await self._playwright.chromium.launch(
            headless=headless,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
        )
        self.context = await self.browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            locale="en-US",
        )
        # 注入 stealth 脚本（绕 navigator.webdriver 等）
        await self.context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            window.chrome = { runtime: {} };
        """)
        self.page = await self.context.new_page()

    async def login(self):
        """登录 Reddit"""
        print("\n[LOGIN] Reddit")
        await self.page.goto("https://www.reddit.com/login", wait_until="domcontentloaded")
        await self.human_delay(2, 4)

        # 填用户名
        username_input = self.page.locator("input[name='username']")
        await username_input.fill(self.config["reddit"]["username"])
        await self.human_delay(0.5, 1.5)

        # 填密码
        password_input = self.page.locator("input[name='password']")
        await password_input.fill(self.config["reddit"]["password"])
        await self.human_delay(0.5, 1.5)

        # 点登录
        await self.page.get_by_role("button", name="Log In").click()
        await self.page.wait_for_url("https://www.reddit.com/", timeout=15000)
        print(f"  [OK] Logged in as {self.config['reddit']['username']}")

    async def browse_subreddit(self, subreddit, minutes=5):
        """浏览 subreddit（养号）"""
        print(f"\n[BROWSE] r/{subreddit} ({minutes} min)")
        await self.page.goto(f"https://www.reddit.com/r/{subreddit}/", wait_until="domcontentloaded")
        await self.human_delay(2, 4)

        end_time = time.time() + minutes * 60
        actions = ["scroll", "click_post", "vote", "next_page"]
        weights = [50, 30, 10, 10]

        while time.time() < end_time:
            action = random.choices(actions, weights=weights)[0]
            try:
                if action == "scroll":
                    scroll_y = random.randint(300, 1200)
                    await self.page.evaluate(f"window.scrollBy(0, {scroll_y})")
                elif action == "click_post":
                    posts = await self.page.locator("[data-testid='post-container']").all()
                    if posts:
                        post = random.choice(posts[:10])
                        await post.click()
                        await self.human_delay(3, 8)
                        # scroll 评论
                        for _ in range(random.randint(1, 3)):
                            await self.page.evaluate(f"window.scrollBy(0, {random.randint(200, 600)})")
                            await self.human_delay(1, 2)
                        await self.page.go_back()
                elif action == "vote":
                    posts = await self.page.locator("[data-testid='post-container']").all()
                    if posts:
                        post = random.choice(posts[:5])
                        # upvote
                        try:
                            upvote = post.locator("button[aria-label*='upvote']").first
                            await upvote.click(timeout=2000)
                        except Exception:
                            pass
                elif action == "next_page":
                    next_btn = self.page.locator("a[rel='next']").first
                    if await next_btn.count():
                        await next_btn.click()
                        await self.human_delay(2, 4)
                await self.human_delay()
            except Exception as e:
                print(f"  [WARN] {action} failed: {str(e)[:60]}")

        print(f"  [OK] Done browsing r/{subreddit}")

    async def post_show_hn(self):
        """发 Show HN 帖"""
        print("\n[POST] Show HN")
        await self.page.goto("https://www.reddit.com/r/SideProject/submit", wait_until="domcontentloaded")
        await self.human_delay(2, 4)

        # 选 text post
        try:
            text_tab = self.page.get_by_role("tab", name="Text")
            await text_tab.click()
            await self.human_delay()
        except Exception:
            pass

        # 标题
        await self.page.locator("textarea[name='title']").fill(self.config["show_hn_draft"]["title"])
        await self.human_delay(1, 2)

        # 正文
        body_path = Path(__file__).parent / self.config["show_hn_draft"]["body_path"]
        if not body_path.exists():
            body_path = Path(self.config["show_hn_draft"]["body_path"])
        body = body_path.read_text(encoding="utf-8")
        # 提取 main body 块
        if "正文" in body:
            body = body.split("正文", 1)[1]
        if "```" in body:
            body = body.split("```", 2)[1] if "```" in body else body
        await self.page.locator("textarea[name='text']").fill(body[:40000])
        await self.human_delay(2, 4)

        # 截图确认
        screenshot = f"reddit_post_{int(time.time())}.png"
        await self.page.screenshot(path=screenshot)
        print(f"  [OK] Screenshot: {screenshot}")
        print(f"  [MANUAL] Review + click Post in browser")
        # 不自动 submit — 用户审核

    async def cleanup(self):
        if self.browser:
            await self.browser.close()
        if self._playwright:
            await self._playwright.stop()


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", choices=["login", "browse", "post", "all"], default="all")
    parser.add_argument("--subreddit", default="SideProject")
    parser.add_argument("--minutes", type=int, default=5)
    parser.add_argument("--no-headless", action="store_true")
    args = parser.parse_args()

    bot = RedditAutomation(CONFIG)
    await bot.launch(headless=not args.no_headless)

    try:
        if args.action in ["login", "all"]:
            await bot.login()
        if args.action in ["browse", "all"]:
            await bot.browse_subreddit(args.subreddit, args.minutes)
        if args.action in ["post", "all"]:
            await bot.post_show_hn()
    finally:
        await bot.cleanup()


if __name__ == "__main__":
    asyncio.run(main())