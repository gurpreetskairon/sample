import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-button\"]")).to_contain_text("Login")
