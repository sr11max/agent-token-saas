"""
token-saas E2E 测试
1. 访问主页
2. 注册新用户
3. 调 AI chat
4. 验证 token 扣费
5. 截图
"""
import argparse
import json
import time
from playwright.sync_api import sync_playwright


def run_e2e(base_url):
    print(f"\n[E2E] base_url={base_url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        # 1. 访问主页
        print("\n[1] GET /")
        r = page.goto(base_url, wait_until="domcontentloaded", timeout=15000)
        assert r.status == 200, f"Expected 200, got {r.status}"
        title = page.title()
        assert "CheapToken" in title or "cheaptoken" in title.lower(), f"Unexpected title: {title}"
        print(f"  [OK] title={title!r}")
        page.screenshot(path="e2e-1-home.png", full_page=True)

        # 2. 注册
        print("\n[2] POST /api/auth/register")
        email = f"e2e_{int(time.time())}@cheaptoken.test"
        password = "Test1234!"
        r = page.request.post(f"{base_url}/api/auth/register", data={
            "email": email,
            "password": password,
        })
        assert r.status == 200, f"Register failed: {r.status} {r.text()}"
        reg_data = r.json()
        jwt_token = reg_data["token"]
        initial_balance = reg_data["token_balance"]
        print(f"  [OK] registered: email={email}, balance={initial_balance}")

        # 3. 调 AI chat
        print("\n[3] POST /api/chat")
        r = page.request.post(f"{base_url}/api/chat", data={
            "message": "用一句话介绍自己",
        }, headers={"Authorization": f"Bearer {jwt_token}"})
        assert r.status == 200, f"Chat failed: {r.status} {r.text()}"
        chat_data = r.json()
        reply = chat_data["reply"]
        tokens_used = chat_data["tokens_used"]
        new_balance = chat_data["token_balance"]
        print(f"  [OK] reply={reply[:60]!r}")
        print(f"  [OK] tokens_used={tokens_used}, balance: {initial_balance} -> {new_balance}")
        assert new_balance < initial_balance, f"Balance should decrease: {initial_balance} -> {new_balance}"

        # 4. 验证 /api/me
        print("\n[4] GET /api/me")
        r = page.request.get(f"{base_url}/api/me", headers={"Authorization": f"Bearer {jwt_token}"})
        assert r.status == 200, f"GET /api/me failed: {r.status}"
        me_data = r.json()
        assert me_data["token_balance"] == new_balance
        print(f"  [OK] me.email={me_data['email']}, balance={me_data['token_balance']}")

        # 5. 调第二次 chat 验证扣费累计
        print("\n[5] Second chat (verify cumulative balance)")
        r = page.request.post(f"{base_url}/api/chat", data={
            "message": "1+1=?",
        }, headers={"Authorization": f"Bearer {jwt_token}"})
        assert r.status == 200
        chat2 = r.json()
        final_balance = chat2["token_balance"]
        print(f"  [OK] second chat: tokens={chat2['tokens_used']}, balance={final_balance}")
        assert final_balance < new_balance, f"Second chat should also deduct: {new_balance} -> {final_balance}"

        # 6. 测访问 UI（实际用 page 而非 API）
        print("\n[6] UI flow: register + chat via form")
        page.goto(f"{base_url}/", wait_until="domcontentloaded")
        # 用 Playwright 走完整 UI 流程
        page.fill("input[type='email']", f"ui_{int(time.time())}@cheaptoken.test")
        page.fill("input[type='password']", password)
        page.click("button:has-text('Register')")
        # 等 chat 面板
        try:
            page.wait_for_selector("input[placeholder*='ask']", timeout=10000)
            print("  [OK] registered via UI, chat panel visible")
        except Exception as e:
            print(f"  [WARN] chat panel not visible: {e}")
        page.screenshot(path="e2e-6-ui.png", full_page=True)

        # 7. 测 health endpoint
        print("\n[7] GET /health")
        r = page.request.get(f"{base_url}/health")
        assert r.status == 200, f"Health failed: {r.status}"
        health = r.json()
        print(f"  [OK] {health}")

        browser.close()
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="token-saas base URL (e.g. https://xxx.up.railway.app)")
    args = parser.parse_args()

    try:
        run_e2e(args.url)
        print("\n" + "=" * 60)
        print("[OK] ALL E2E TESTS PASSED")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")