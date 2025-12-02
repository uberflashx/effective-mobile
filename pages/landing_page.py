from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.about_link = page.locator('//a[contains(@href, "about")]')
        self.about_block = page.locator('section#about')
        self.vacancies_link = page.locator('//a[contains(@href, "specializations")]')
        self.reviews_link = page.locator('//a[contains(@href, "testimonials")]')
        self.contacts_link = page.locator('//a[contains(@href, "contact")]')

        self.outstaff_link = page.locator('//a[contains(@href, "services")]').nth(0)
        self.outstaff_block = page.locator('section#services')
        self.employment_link = page.locator('//a[contains(@href, "services")]').nth(1)
        self.callback_link = page.locator('//a[contains(@href, "contact")]')

    def outstaff_link_redirect(self):
        self.outstaff_link.click()
        expect(self.outstaff_block).to_be_visible()

    def about_link_redirect(self):
        self.about_link.click()
        expect(self.about_block).to_be_visible()