import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    headless = os.getenv("HEADLESS", "true").lower() != "false"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        page = browser.new_page()
        page.set_default_timeout(10_000)
        yield page
        browser.close()
