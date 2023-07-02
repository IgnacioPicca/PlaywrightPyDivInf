from playwright.sync_api import sync_playwright

from login import login
from newClient import create_new_client

linkWeb = "http://loanhomologacion.dash-deportes.com.ar/"


def main():
    with sync_playwright() as p:
        # Open browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(linkWeb)

        # Login
        login(page)

        # Create New Client
        create_new_client(page)

        # Close browser
        browser.close()


if __name__ == "__main__":
    main()
