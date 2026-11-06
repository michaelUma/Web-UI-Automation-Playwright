# Web UI Automation with Playwright and Python

Browser automation portfolio using Playwright's Python API and Pytest.

## Practice target
SauceDemo (https://www.saucedemo.com/), a public demo shopping application. Use only its published demo credentials and normal user flows. Do not perform load or destructive security testing.

## Skills demonstrated
- Browser lifecycle and fixtures
- Locators and user interactions
- Login success and failure paths
- Assertions and condition-based waits
- Page Object Model
- Headless/headed execution

## Setup
```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Run
```bash
pytest -v
```
Set `HEADLESS=false` to view the browser while tests run.

## Structure
- `pages/login_page.py` — Page Object Model
- `ui_tests/test_login.py` — login scenarios
- `conftest.py` — browser fixture
- `docs/TEST-STRATEGY.md` — locator and reliability guidance

## Scenarios
- Login page and fields are visible.
- Valid demo user reaches inventory.
- Invalid password displays an error.
- Logout returns to login.

## Good practices
Prefer accessible role/label locators and stable test IDs. Wait for observable conditions rather than fixed sleeps. Keep tests independent and credentials out of source control.

## Author
Michael Uma — UI Test Automation Portfolio.
