from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_flash_text(self) -> str:
        return self.flash_message.inner_text()
