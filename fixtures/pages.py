import pytest
from playwright.sync_api import Page

from pages.landing_page import LandingPage


@pytest.fixture
def landing_page(chromium_page: Page) -> LandingPage:
    return LandingPage(page=chromium_page)