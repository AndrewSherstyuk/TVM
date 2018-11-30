import allure
from pages.Flixon.SigninPage import *
from pages.Flixon.PageHeader import *
from core.globals import *
from core.randomizer import *

correct_email = "0000@0000.com"
correct_password = "010101"
incorrect_email = Randomizer.email()
incorrect_password = Randomizer.password(size=6)


@allure.title("Sign In page initial state verification")
@allure.description("""The test opens the Sign In page and verifies that all its elements are available""")
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


@allure.title("Sign In page: Successful Sign In")
@allure.description("""The test verifies that Sign In functions as expected: the user is able to
successfully sign in.""")
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


@allure.title("Sign In page: Unsuccessful Sign In with incorrect password")
@allure.description("""The test verifies that Sign In functions as expected: the user is unable to sign in
using the wrong password.""")
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


@allure.title("Sign In page: Unsuccessful Sign In with the Password left empty")
@allure.description("""The test verifies that Sign In functions as expected: the user is unable to sign in
if the Password field is left empty""")
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


@allure.title("Sign In page: Unsuccessful Sign In with incorrect email")
@allure.description("""The test verifies that Sign In functions as expected: the user is unable to sign in
with a wrong email.""")
def test_unsuccessful_login_incorrect_email():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with non-existing user's email"):
        SigninPage().fill_in_the_username_field(incorrect_email)
    with allure.step("Fill in the Password field with existing user's Password"):
        SigninPage().fill_in_the_password_field(correct_password)
    with allure.step("Submit login"):
        SigninPage().submit_login()
    with allure.step("Verify the Login error message"):
        SigninPage().check_login_error_message()
    browser.quit_driver()


@allure.title("Sign In page: Unsuccessful Sign In with the Email left empty")
@allure.description("""The test verifies that Sign In functions as expected: the user is unable to sign in
if the Email field is left empty""")
def test_unsuccessful_login_empty_email_field():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Fill in the Email field with existing user's email"):
        SigninPage().fill_in_the_password_field(correct_password)
    with allure.step("Submit login with empty Email field"):
        SigninPage().submit_login()
    with allure.step("Verify that the user is still logged out"):
        SigninPage().check_that_signin_page_is_still_displayed()
    browser.quit_driver()


@allure.title("Sign In page: Unsuccessful Sign In with the Password and Email fields left empty")
@allure.description("""The test verifies that Sign In functions as expected: the user is unable to sign in
if the Password and Email fields are left empty""")
def test_unsuccessful_login_empty_email_and_password_fields():
    with allure.step("Open url: " + BASE_URL):
        browser.open_url(BASE_URL)
    with allure.step("Click on the Sign In button"):
        SigninPage().tap_on_sign_in()
    with allure.step("Submit login with empty Email and Password field"):
        SigninPage().submit_login()
    with allure.step("Verify that the user is still logged out"):
        SigninPage().check_that_signin_page_is_still_displayed()
    browser.quit_driver()


@allure.title("Successful Sign Out")
@allure.description("""The test verifies that Sign Out functions as expected: the user is able to
successfully sign out to the site.""")
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
        PageHeader().click_on_signout_btn()
    with allure.step("Click Yes on Logout confirmation"):
        PageHeader().confirm_wish_to_logout()
    with allure.step("Verify that the user is logged out"):
        SigninPage().sign_in_btn.should(be.visible)
    browser.quit_driver()


@allure.title("Sign Out: No is selected on the Sign Out Confirmation popup")
@allure.description("""The test verifies that Sign Out functions as expected: the user is able to
cancel sign out by selecting No on the Sign Out confirmation popup.""")
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
        PageHeader().click_on_signout_btn()
    with allure.step("Click No on Logout confirmation"):
        PageHeader().confirm_wish_to_not_logout()
    with allure.step("Verify the user is still logged in"):
        PageHeader().sign_out_btn.should(be.visible)
    browser.quit_driver()
