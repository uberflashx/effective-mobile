import pytest
from playwright.sync_api import Page, expect
from pages.landing_page import LandingPage

def test_footer_link_redirections(chromium_page: Page):
    landing_page = LandingPage(page=chromium_page)
    landing_page.visit('https://www.effective-mobile.ru')
    landing_page.outstaff_link_redirect()
    landing_page.about_link_redirect()
