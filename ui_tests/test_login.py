from pages.login_page import LoginPage


def test_login_page_is_visible(page):
    login = LoginPage(page).open()
    assert login.login_button.is_visible()
    assert login.username.is_visible()
    assert login.password.is_visible()


def test_valid_demo_user_can_log_in(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    assert page.get_by_text("Products").is_visible()
    assert page.locator(".inventory_item").count() > 0


def test_invalid_password_shows_error(page):
    login = LoginPage(page).open()
    login.login("standard_user", "wrong-password")
    assert page.locator("[data-test='error']").is_visible()


def test_logout_returns_to_login(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
    assert page.get_by_role("button", name="Login").is_visible()
