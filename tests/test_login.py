from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# ---------- SUCCESSFUL LOGIN TEST ----------

def test_successful_login(page: Page):
    """
    Verify that a user can log in with valid credentials.
    Uses the public demo app: https://the-internet.herokuapp.com/login
    """
    login_page = LoginPage(page)

    # 1. Go to login page
    login_page.goto()

    # 2. Perform login with valid credentials
    login_page.login("tomsmith", "SuperSecretPassword!")

    # 3. Assert that a success message is shown
    expect(login_page.flash_message).to_contain_text("You logged into a secure area!")


# ---------- INVALID LOGIN TEST WITH SCREENSHOT ON UNEXPECTED PASS ----------

def test_login_with_invalid_credentials(page: Page, tmp_path):
    """
    Verify that login fails with invalid credentials.
    If login unexpectedly succeeds, capture a screenshot for debugging.
    """
    login_page = LoginPage(page)

    # 1. Go to login page
    login_page.goto()

    # 2. Use invalid credentials
    login_page.login("invalid_user", "wrong_password")

    flash_text = login_page.get_flash_text()

    # 3. If somehow it logs in (unexpected), capture screenshot
    if "You logged into a secure area!" in flash_text:
        screenshot_path = tmp_path / "unexpected_success.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        assert False, f"Login succeeded with invalid credentials, screenshot: {screenshot_path}"

    # 4. Normal expectation: invalid username message
    expect(login_page.flash_message).to_contain_text("Your username is invalid!")
