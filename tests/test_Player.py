import allure
import time
from pages.SigninPage import *
from pages.GuidePage import *
from pages.PageHeader import *
from pages.PlayerPage import *
from core.globals import *
from core.randomizer import *

correct_email = "0000@0000.com"
correct_password = "010101"
#
# @allure.title("Video Player: Home button verification")
# @allure.description("""The test opens video player from the Guide page, taps on the Home button and verifies that the Guide screen opens""")
# def test_signin_page_initial_state():
#     with allure.step("Sign In as an existing user"):
#         SigninPage().login_as_user(correct_email, correct_password)
#     # with allure.step("Open url: " + "http://flixon.tvmucho.com/#live/200665"):
#     #     browser.open_url("http://flixon.tvmucho.com/#live/200665")
#     #     time.sleep(10)
#     with allure.step("Tap on the first channel in the list"):
#         time.sleep(5)
#         GuidePage().first_channel_in_the_list.click()
#     with allure.step("Get the player controls visible"):
#         PlayerPage().click_on_the_player_to_unhide_controls()
#     with allure.step("Tap on the Home button"):
#         PlayerPage().tap_on_home_button()
#     with allure.step("Verify that the Guide page is opened"):
#         GuidePage().day_selector.should(be.visible)
#         browser.quit_driver()

@allure.title("Video Player: Channels button verification")
@allure.description(
    """The test opens video player, taps on the Channels button and verifies that the Channels list gets visible""")
def test_signin_page_initial_state():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user(correct_email, correct_password)
        time.sleep(5)
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(15)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        print("D Click")
        PlayerPage().player_window.hover()
        print("Hover")
    with allure.step("Tap on the Home button"):
         PlayerPage().tap_on_channels_button()
         #time.sleep(10)
    with allure.step("Verify that the channels line got visible"):
         PlayerPage().channels_left_arrow_button.click()
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # with allure.step("Verify the page title"):
    #     element = browser.title()
    #     assert element == "Flixon TV"
    # with allure.step("Verify that logo is visible"):
    #     SigninPage().logo.should(be.visible)
    # with allure.step("Verify that welcome window is visible"):
    #     SigninPage().welcome_window.should(be.visible)
    # with allure.step("Verify that welcome text matches the requirements"):
    #     SigninPage().welcome_text.should(have.text('Welcome to Flixon TV...'))
    # with allure.step("Verify that Sign in button is clickable"):
    #     SigninPage().sign_in_btn.should(be.visible).should(be.clickable)
    #     assert SigninPage().sign_in_btn.text == "SIGN IN"
    # browser.quit_driver()
    #
    # @allure.title("Sign In page: Successful Sign In")
    # @allure.description("""The test verifies that Sign In functions as expected: the user is able to
    # successfully sign in.""")
    # def test_successful_login():
    #     with allure.step("Open url: " + BASE_URL):
    #         browser.open_url(BASE_URL)
    #     with allure.step("Click on the Sign In button"):
    #         SigninPage().tap_on_sign_in()
    #     with allure.step("Fill in the Email field with existing user's email"):
    #         SigninPage().fill_in_the_username_field(correct_email)
    #     with allure.step("Fill in the Password field with existing user's password"):
    #         SigninPage().fill_in_the_password_field(correct_password)
    #     with allure.step("Submit login"):
    #         SigninPage().submit_login()
    #     with allure.step("Verify that the Guide page is opened"):
    #         GuidePage().day_selector.should(be.visible)
    #     browser.quit_driver()
