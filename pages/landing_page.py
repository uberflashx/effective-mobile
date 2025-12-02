from pages.base_page import BasePage
from playwright.sync_api import Page

class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.about_link = page.locator('//a[contains(@href, "about")]')

    def click_about_link(self):
        self.about_link.click()