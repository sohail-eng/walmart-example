from playwright.sync_api import sync_playwright

import requests


def get_cookies(url: str):
    response = requests.get("http://localhost:9222/json/version")
    data = response.json()
    browser_id = data.get("webSocketDebuggerUrl").split('/')[-1]

    cookies = {}

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"ws://localhost:9222/devtools/browser/{browser_id}")
        page = browser.new_page()
        page.goto(url)

        cookies = page.context.cookies()
        cookies = {cookie['name']: cookie['value'] for cookie in cookies}
    return cookies

if __name__ == "__main__":
     cookies = get_cookies(url="https://www.walmart.com/ip/LEGO-Technic-tbd-42200/6924164794")
     print(cookies)
