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


@allure.title("Video Player: Home button verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Home button and verifies that the Guide screen opens""")
def test_player_home_button_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Tap on the Home button"):
        PlayerPage().tap_on_home_button()
        time.sleep(1)
    with allure.step("Verify that the Guide page is opened"):
        GuidePage().day_selector.should(be.visible)
        browser.quit_driver()


@allure.title("Video Player: Channels button verification")
@allure.description(
    """The test opens video player, taps on the Channels button and verifies that the Channels list gets visible.""")
def test_player_channels_button_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Tap on the Channels button"):
        PlayerPage().tap_on_channels_button()
    with allure.step("Verify that the channels line got visible"):
        PlayerPage().channels_left_arrow_button.should(be.visible)
        PlayerPage().channels_right_arrow_button.should(be.visible)
    with allure.step("Wait for the Player controls to get hidden"):
        time.sleep(10)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Verify that the Channels List is not displayed any longer"):
        PlayerPage().channels_button.should(be.visible)
        time.sleep(1)
        browser.quit_driver()

@allure.title("Video Player: Favourite button verification")
@allure.description("""The test opens video player from the Guide page, taps
    on the Favourite button and verifies its selected and unselected states""")
def test_player_favourite_button_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
    with allure.step("Verify that the Favourite button is not clicked"):
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart-o'))
    with allure.step("Wait for the Player controls to disappear"):
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Verify that the Favourite button is still not clicked"):
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart-o'))
    with allure.step("Click on the Favourite button"):
        PlayerPage().favorite_button.click()
    with allure.step("Verify that the Favourite button is clicked"):
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart'))
    with allure.step("Click on the Favourite button again to make the event not favourite again"):
        PlayerPage().favorite_button.click()
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart-o'))
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Play/Stop button verification")
@allure.description("""The test opens video player from the Guide page, taps
        on the Playstop button and verifies its Stop and Play states""")
def test_player_playstop_button_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Verify that the Playstop button is in the Stop state"):
            PlayerPage().playstop_stop_button.should(be.visible)
        with allure.step("Wait for the Player controls to disappear"):
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Verify that the Playstop button is still in the stop state"):
            PlayerPage().playstop_stop_button.should(be.visible)
        with allure.step("Click on the Playstop button"):
            PlayerPage().playstop_stop_button.click()
        with allure.step("Verify that the Playstop button is in the Play state"):
            PlayerPage().playstop_play_button.should(be.visible)
        with allure.step("Click on the Playstop button again to verify that it's in Stop state again"):
            PlayerPage().playstop_play_button.click()
            PlayerPage().playstop_stop_button.should(be.visible)
            time.sleep(1)
            browser.quit_driver()


@allure.title("Video Player: Closed Captions button verification")
@allure.description("""The test opens video player from the Guide page, taps
        on the CC button and verifies its functionality""")
def test_player_closed_captions_button_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Wait for the Player controls to disappear"):
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the CC button"):
            PlayerPage().cc_menu_button.click()
        with allure.step("Select the English option from the CC menu"):
            PlayerPage().cc_menu_english_option.click()

        #     # Here we need to check that the subtitles are actually visible

        with allure.step("Click on the CC button"):
            PlayerPage().cc_menu_button.click()
        with allure.step("Select the Off option from the CC menu"):
            PlayerPage().cc_menu_off_option.click()

        #     # Here we need to check that the subtitles are not displayed any longer

            browser.quit_driver()


@allure.title("Video Player: Help menu > Help form > Close button verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Help button, selects Something Wrong... options and verifies the Close option on the Help form""")
def test_player_help_somethingwrong_option_verification_1():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Wait for the Player controls to disappear"):
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the Help button"):
            PlayerPage().help_button.click()
            time.sleep(1)
        with allure.step("Verify that the Help panel gets shown"):
            PlayerPage().help_panel.should(be.visible)
            time.sleep(1)
        with allure.step("Select 'Something Wrong...' option"):
            PlayerPage().somethingwrong_option.click()
            time.sleep(1)
        with allure.step("Verify that the Help form gets opened"):
            PlayerPage().help_form.should(be.visible)
            time.sleep(1)
        with allure.step("Click/tap on the Close button of the Help form"):
            PlayerPage().help_form_close_button.click()
        with allure.step("Verify that the Help form and the Player controls get hidden"):
            PlayerPage().help_button.should(be.visible)
            browser.quit_driver()


@allure.title("Video Player: Help menu > Help form > Confirm button selected with empty Help form verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Help button, selects Something Wrong... option, leaves the Help form empty and confirms, then verifies the tvm-popup""")
def test_player_help_somethingwrong_option_verification_2():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Wait for the Player controls to disappear"):
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the Help button"):
            PlayerPage().help_button.click()
            time.sleep(1)
        with allure.step("Select 'Something Wrong...' option"):
            PlayerPage().somethingwrong_option.click()
            time.sleep(1)
        with allure.step("Click/tap on the Submit button of the Help form"):
            PlayerPage().help_form_submitreport_button.click()
        with allure.step("Verify that the tvm-popup gets visible and looks as expected"):
            PlayerPage().help_form_empty_report_notification.should(be.visible)
            PlayerPage().help_form_empty_report_notification_title.should(be.visible)
            PlayerPage().help_form_empty_report_notification_message.should(be.visible)
        with allure.step("Confirm the empty Help form "):
            PlayerPage().help_form_empty_report_notification_conrim_button.click()
        with allure.step("Verify that the tvm-popup gets closed and the Help form is displayed again"):
            PlayerPage().help_form.should(be.visible)
            browser.quit_driver()


@allure.title("Video Player: Help menu > Help form > Text into the input field > Confirm button selected verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Help button, selects Something Wrong... option, adds some text into the input field on the Help form and confirms, then verifies the tvm-popup""")
def test_player_help_somethingwrong_option_verification_3():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Wait for the Player controls to disappear"):
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the Help button"):
            PlayerPage().help_button.click()
            time.sleep(1)
        with allure.step("Select 'Something Wrong...' option"):
            PlayerPage().somethingwrong_option.click()
            time.sleep(1)
        with allure.step("Add the test text into the Report Message field"):
            PlayerPage().help_form_input_field.set_value("Test report, please disregard. Please contact Andrey Sherstyuk, TVM QA Engineer for more information.")
        with allure.step("Click/tap on the Close button of the Help form"):
            PlayerPage().help_form_submitreport_button.click()
            time.sleep(15)
        with allure.step("Verify that the Report Received notification is displayed"):
            PlayerPage().help_form_report_received_notification.should(be.visible)
        with allure.step("Click on the Continue button on the Report Received notification"):
            PlayerPage().help_form_report_received_notification_confirm_button.click()
            time.sleep(5)
        with allure.step("Verify that the video playback is displayed"):
            PlayerPage().help_button.should_not(be.visible)
            PlayerPage().help_form_report_received_notification.should_not(be.visible)
            browser.quit_driver()


@allure.title("Video Player: Help menu > Show Playback Stats verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Help button, selects Show Playback Stats option, and verifies that the Playback Stats popup shows up""")
def test_player_help_somethingwrong_option_verification_4():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Wait for the Player controls to disappear"):
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the Help button"):
            PlayerPage().help_button.click()
            time.sleep(1)
        with allure.step("Select Show Playback Stats option"):
            PlayerPage().showplaybackstats_option.click()
            time.sleep(1)
        with allure.step("Verify that the Playback Stats popup shows up"):
            PlayerPage().playbackstats_popup.should(be.visible)
            time.sleep(3)
        with allure.step("Close the Playback Stats popup"):
            PlayerPage().playbackstats_popup_close_button.click()
        with allure.step("Verify that the Playback Stats popup gets closed"):
            PlayerPage().playstop_stop_button.should(be.visible)
            time.sleep(7)
            PlayerPage().playstop_stop_button.should_not(be.visible)
            browser.quit_driver()


@allure.title("Video Player: Help menu > Reload Stream option verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Help button, selects Show Playback Stats option, and verifies that the Playback Stats popup shows up""")
def test_player_help_reloadstream_option_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Wait for the Player controls to disappear"):
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the Help button"):
            PlayerPage().help_button.click()
            time.sleep(1)
        with allure.step("Select Show Playback Stats option"):
            PlayerPage().showplaybackstats_option.click()
            time.sleep(1)
        with allure.step("Verify that the Playback Stats popup shows up"):
            PlayerPage().playbackstats_popup.should(be.visible)
            time.sleep(3)
        with allure.step("Close the Playback Stats popup"):
            PlayerPage().playbackstats_popup_close_button.click()
        with allure.step("Verify that the Playback Stats popup gets closed"):
            PlayerPage().playstop_stop_button.should(be.visible)
            time.sleep(7)
            PlayerPage().playstop_stop_button.should_not(be.visible)
            browser.quit_driver()









            # with allure.step("Verify that the Favourite button is clicked"):
        #     PlayerPage().playstop_play_button.should(be.visible)
        # with allure.step("Click on the Favourite button again to make the event not favourite again"):
        #     PlayerPage().playstop_play_button.click()
        #     PlayerPage().playstop_stop_button.should(be.visible)
        #     time.sleep(1)
        #     browser.quit_driver()



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
