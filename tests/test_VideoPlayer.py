import allure
from pages.SigninPage import *
from pages.PageHeader import *
from core.globals import *
from core.randomizer import *

@allure.title("Video Player: Home button verification")
@allure.description("""The test opens video player from the Guide page, taps on the Home button and verifies that the Home screen opens""")
def test_signin_page_initial_state():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Verify the page title"):
        element = browser.title()
        assert element == "Flixon TV"
    with allure.step("Verify that logo is visible"):
        SigninPage().logo.should(be.visible)
    with allure.step("Verify that welcome window is visible"):
        SigninPage().welcome_window.should(be.visible)
    with allure.step("Verify that welcome text matches the requirements"):
        SigninPage().welcome_text.should(have.text('Welcome to Flixon TV...'))
    with allure.step("Verify that Sign in button is clickable"):
        SigninPage().sign_in_btn.should(be.visible).should(be.clickable)
        assert SigninPage().sign_in_btn.text == "SIGN IN"
    browser.quit_driver()