import asyncio
from playwright.async_api import async_playwright
from login import login
from newClient import create_new_client

linkWeb = "http://loanhomologacion.dash-deportes.com.ar/"


async def main():
    async with async_playwright() as p:
        # Open browser
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto(linkWeb)

        # Login
        await login(page)

        # Create New Client
        await create_new_client(page)

        # Close browser
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
