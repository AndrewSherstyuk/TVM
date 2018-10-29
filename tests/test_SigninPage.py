import allure
from pages.SigninPage import *
from pages.GuidePage import *
from core.globals import *
from core.randomizer import *

correct_email = "0000@0000.com"
correct_password = "000000"
incorrect_email = Randomizer.email()
incorrect_password = Randomizer.password(size=6)


@allure.title("Welcome Page showing")
@allure.description("""This test opens BASE URL and checks that Welcome Page is shown to user. 
And it contains all required elements.""")
def test_signin_page_initial_state():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Check page's title"):
        element = browser.title()
        assert element == "Flixon TV"
    with allure.step("Check that logo is visible"):
        SigninPage().logo.should(be.visible)
    with allure.step("Check that welcome window is visible"):
        SigninPage().welcome_window.should(be.visible)
    with allure.step("Check that welcome text matches with expected"):
        SigninPage().welcome_text.should(have.text('Welcome to Flixon TV...'))
    with allure.step("Check that Sign in button is clickable and moves user to Sign In page"):
        SigninPage().sign_in_btn.should(be.visible).should(be.clickable)
        assert SigninPage().sign_in_btn.text == "SIGN IN"
    browser.quit_driver()


def test_successful_login():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with existing user's email"):
        SigninPage().fill_in_the_username_field(correct_email)
    with allure.step("Fill in the Password field with existing user's password"):
        SigninPage().fill_in_the_password_field(correct_password)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Verify that the Guide page is opened"):
        GuidePage().day_selector.should(be.visible)
    browser.quit_driver()


def test_unsuccessful_login_incorrect_password():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with existing user's email"):
        SigninPage().fill_in_the_username_field(correct_email)
    with allure.step("Fill in the Password field with existing user's Password"):
        SigninPage().fill_in_the_password_field(incorrect_password)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Verify that the Login error message is displayed"):
        SigninPage().check_login_error_message()
    browser.quit_driver()


def test_unsuccessful_login_empty_password_field():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with existing user's email"):
        SigninPage().fill_in_the_username_field(correct_email)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Verify that the Sign In page is still displayed"):
        SigninPage().check_that_signin_page_is_still_displayed()
    browser.quit_driver()


def test_unsuccessful_login_incorrect_email():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with non-existing   user's email"):
        SigninPage().fill_in_the_username_field(incorrect_email)
    with allure.step("Fill in the Password field with existing user's Password"):
        SigninPage().fill_in_the_password_field(correct_password)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Check the Login error message"):
        SigninPage().check_login_error_message()
    browser.quit_driver()


def test_unsuccessful_login_empty_email_field():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with existing user's email"):
        SigninPage().fill_in_the_password_field(correct_password)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Verify that the Sign In page is still displayed"):
        SigninPage().check_that_signin_page_is_still_displayed()
    browser.quit_driver()


def test_logout():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with existing user's email"):
        SigninPage().fill_in_the_username_field(correct_email)
    with allure.step("Fill in the Password field with existing user's Password"):
        SigninPage().fill_in_the_password_field(correct_password)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Verify that the Guide page is opened"):
        GuidePage().day_selector.should(be.visible)
    with allure.step("Click on Logout button"):
        GuidePage().click_on_signout_btn()
    with allure.step("Click Yes on Logout confirmation"):
        GuidePage().confirm_wish_to_logout()
    with allure.step("Verify that the user is logged out"):
        SigninPage().sign_in_btn.should(be.visible)
    browser.quit_driver()


def test_no_button_on_logout_confirmation():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with existing user's email"):
        SigninPage().fill_in_the_username_field(correct_email)
    with allure.step("Fill in the Password field with existing user's Password"):
        SigninPage().fill_in_the_password_field(correct_password)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Verify that the Guide page is opened"):
        GuidePage().day_selector.should(be.visible)
    with allure.step("Click on Logout button"):
        GuidePage().click_on_signout_btn()
    with allure.step("Click No on Logout confirmation"):
        GuidePage().confirm_wish_to_not_logout()
    with allure.step("Verify the user is still logged in"):
        GuidePage().sign_out_btn.should(be.visible)
    browser.quit_driver()
