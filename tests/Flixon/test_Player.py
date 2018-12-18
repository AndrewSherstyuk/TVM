import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *






# @allure.title("Video Player: Play/Stop button verification")
# @allure.description("""The test opens video player from the Guide page, taps
#         on the Playstop button and verifies its Stop and Play states""")
# def test_player_playstop_button_verification():
#         with allure.step("Sign In as an existing user"):
#             SigninPage().login_as_user()
#         with allure.step("Tap on the first channel in the list"):
#             GuidePage().first_channel_in_the_list.click()
#             time.sleep(9)
#         with allure.step("Get the player controls visible"):
#             PlayerPage().player_window.double_click()
#             PlayerPage().player_window.hover()
#         with allure.step("Verify that the Playstop button is still in the stop state"):
#             PlayerPage().playstop_stop_button.should(be.visible)
#         with allure.step("Click on the Playstop button"):
#             PlayerPage().playstop_stop_button.click()
#             time.sleep(1)
#         with allure.step("Verify that the Playstop button is in the Play state"):
#             PlayerPage().playstop_play_button.should(be.visible)
#             time.sleep(1)
#             browser.quit_driver()
#
#
# @allure.title("Video Player: Closed Captions button verification")
# @allure.description("""The test opens video player from the Guide page, taps
#         on the CC button and verifies its functionality""")
# def test_player_closed_captions_button_verification():
#         with allure.step("Sign In as an existing user"):
#             SigninPage().login_as_user()
#         with allure.step("Tap on the first channel in the list"):
#             GuidePage().first_channel_in_the_list.click()
#             time.sleep(9)
#         with allure.step("Get the player controls visible"):
#             PlayerPage().player_window.double_click()
#             PlayerPage().player_window.hover()
#         with allure.step("Click on the CC button"):
#             PlayerPage().cc_menu_button.click()
#         with allure.step("Select the English option from the CC menu"):
#             try:
#                 PlayerPage().cc_menu_english_option.click()
#             except:
#                 pass
#
#
#         #     # Here we need to check that the subtitles are actually visible
#
#         with allure.step("Click on the CC button"):
#             PlayerPage().cc_menu_button.click()
#         with allure.step("Select the Off option from the CC menu"):
#             PlayerPage().cc_menu_off_option.click()
#
#         #     # Here we need to check that the subtitles are not displayed any longer
#
#             browser.quit_driver()
#
#
# @allure.title("Video Player: Help menu > Help form > Close button verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Help button, selects Something Wrong... options and verifies the Close option on the Help form""")
# def test_player_help_something_wrong_option_verification_1():
#     with allure.step("Sign In as an existing user"):
#         SigninPage().login_as_user()
#     with allure.step("Tap on the first channel in the list"):
#         GuidePage().first_channel_in_the_list.click()
#         time.sleep(9)
#     with allure.step("Get the player controls visible"):
#         PlayerPage().player_window.double_click()
#         PlayerPage().player_window.hover()
#     with allure.step("Click on the Help button"):
#         PlayerPage().help_button.click()
#         time.sleep(1)
#     with allure.step("Verify that the Help panel gets shown"):
#         PlayerPage().help_panel.should(be.visible)
#         time.sleep(1)
#     with allure.step("Select 'Something Wrong...' option"):
#         PlayerPage().somethingwrong_option.click()
#         time.sleep(1)
#     with allure.step("Verify that the Help form gets opened"):
#         PlayerPage().help_form.should(be.visible)
#         time.sleep(1)
#     with allure.step("Click/tap on the Close button of the Help form"):
#         PlayerPage().help_form_close_button.click()
#     with allure.step("Verify that the Help form and the Player controls get hidden"):
#         PlayerPage().help_button.should(be.visible)
#         browser.quit_driver()
#
#
# @allure.title("Video Player: Help menu > Help form > Confirm button selected with empty Help form verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Help button, selects Something Wrong... option, leaves the Help form empty and confirms, then verifies the tvm-popup""")
# def test_player_help_something_wrong_option_verification_2():
#     with allure.step("Sign In as an existing user"):
#         SigninPage().login_as_user()
#     with allure.step("Tap on the first channel in the list"):
#         GuidePage().first_channel_in_the_list.click()
#         time.sleep(9)
#     with allure.step("Get the player controls visible"):
#         PlayerPage().player_window.double_click()
#         PlayerPage().player_window.hover()
#     with allure.step("Click on the Help button"):
#         PlayerPage().help_button.click()
#         time.sleep(1)
#     with allure.step("Select 'Something Wrong...' option"):
#         PlayerPage().somethingwrong_option.click()
#         time.sleep(1)
#     with allure.step("Click/tap on the Submit button of the Help form"):
#         PlayerPage().help_form_submitreport_button.click()
#     with allure.step("Verify that the tvm-popup gets visible and looks as expected"):
#         PlayerPage().help_form_empty_report_notification.should(be.visible)
#         PlayerPage().help_form_empty_report_notification_title.should(be.visible)
#         PlayerPage().help_form_empty_report_notification_message.should(be.visible)
#     with allure.step("Confirm the empty Help form "):
#         PlayerPage().help_form_empty_report_notification_conrim_button.click()
#     with allure.step("Verify that the tvm-popup gets closed and the Help form is displayed again"):
#         PlayerPage().help_form.should(be.visible)
#         browser.quit_driver()
#
#
# @allure.title("Video Player: Help menu > Help form > Text into the input field > Confirm button selected verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Help button, selects Something Wrong... option, adds some text into the input field on the Help form and confirms, then verifies the tvm-popup""")
# def test_player_help_something_wrong_option_verification_3():
#     with allure.step("Sign In as an existing user"):
#         SigninPage().login_as_user()
#     with allure.step("Tap on the first channel in the list"):
#         GuidePage().first_channel_in_the_list.click()
#         time.sleep(9)
#     with allure.step("Get the player controls visible"):
#         PlayerPage().player_window.double_click()
#         PlayerPage().player_window.hover()
#     with allure.step("Click on the Help button"):
#         PlayerPage().help_button.click()
#         time.sleep(1)
#     with allure.step("Select 'Something Wrong...' option"):
#         PlayerPage().somethingwrong_option.click()
#         time.sleep(1)
#     with allure.step("Add the test text into the Report Message field"):
#         PlayerPage().help_form_input_field.set_value(
#             "Test report, please disregard. Please contact Andrey Sherstyuk, TVM QA Engineer for more information.")
#     with allure.step("Click/tap on the Close button of the Help form"):
#         PlayerPage().help_form_submitreport_button.click()
#         time.sleep(15)
#     with allure.step("Verify that the Report Received notification is displayed"):
#         PlayerPage().help_form_report_received_notification.should(be.visible)
#     with allure.step("Click on the Continue button on the Report Received notification"):
#         PlayerPage().help_form_report_received_notification_confirm_button.click()
#         time.sleep(5)
#     with allure.step("Verify that the video playback is displayed"):
#         PlayerPage().help_button.should_not(be.visible)
#         PlayerPage().help_form_report_received_notification.should_not(be.visible)
#         browser.quit_driver()
#
#
# @allure.title("Video Player: Help menu > Show Playback Stats verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Help button, selects Show Playback Stats option, and verifies that the Playback Stats popup shows up""")
# def test_player_help_something_wrong_option_verification_4():
#     with allure.step("Sign In as an existing user"):
#         SigninPage().login_as_user()
#     with allure.step("Tap on the first channel in the list"):
#         GuidePage().first_channel_in_the_list.click()
#         time.sleep(9)
#     with allure.step("Get the player controls visible"):
#         PlayerPage().player_window.double_click()
#         PlayerPage().player_window.hover()
#     with allure.step("Click on the Help button"):
#         PlayerPage().help_button.click()
#         time.sleep(1)
#     with allure.step("Select Show Playback Stats option"):
#         PlayerPage().showplaybackstats_option.click()
#         time.sleep(1)
#     with allure.step("Verify that the Playback Stats popup shows up"):
#         PlayerPage().playbackstats_popup.should(be.visible)
#         time.sleep(3)
#     with allure.step("Close the Playback Stats popup"):
#         PlayerPage().playbackstats_popup_close_button.click()
#     with allure.step("Verify that the Playback Stats popup gets closed"):
#         PlayerPage().playstop_stop_button.should(be.visible)
#         time.sleep(7)
#         PlayerPage().playstop_stop_button.should_not(be.visible)
#         browser.quit_driver()


@allure.title("Video Player: Help menu > Reload Stream option verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Help button, selects Show Playback Stats option, and verifies that the Playback Stats popup shows up""")
def test_player_help_reload_stream_option_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Click on the Help button"):
        PlayerPage().help_button.click()
        time.sleep(1)
    with allure.step("Select Show Playback Stats option"):
        PlayerPage().reloadstream_option.click()
        time.sleep(1)
    with allure.step("Verify that the Playback Stats popup gets closed"):
        PlayerPage().playstop_stop_button.should(be.visible)
        time.sleep(7)
        PlayerPage().playstop_stop_button.should_not(be.visible)
        browser.quit_driver()


# @allure.title("Video Player: Help menu > Close option verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Help button, selects Close option, and verifies that the Help panel disappears""")
# def test_player_help_close_option_verification():
#     with allure.step("Sign In as an existing user"):
#         SigninPage().login_as_user()
#     with allure.step("Tap on the first channel in the list"):
#         GuidePage().first_channel_in_the_list.click()
#         time.sleep(9)
#     with allure.step("Get the player controls visible"):
#         PlayerPage().player_window.double_click()
#         PlayerPage().player_window.hover()
#     with allure.step("Click on the Help button"):
#         PlayerPage().help_button.click()
#         time.sleep(1)
#     with allure.step("Select Show Playback Stats option"):
#         PlayerPage().close_option.click()
#         time.sleep(1)
#     with allure.step("Verify that the Playback of the video shows up"):
#         PlayerPage().playstop_stop_button.should(be.visible)
#         time.sleep(7)
#         PlayerPage().playstop_stop_button.should_not(be.visible)
#         browser.quit_driver()
#
#
# @allure.title("Video Player: Volume button verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Volume button, TBD               """)
# def test_player_volume_button_verification():
#         with allure.step("Sign In as an existing user"):
#             SigninPage().login_as_user()
#         with allure.step("Tap on the first channel in the list"):
#             GuidePage().first_channel_in_the_list.click()
#             time.sleep(9)
#         with allure.step("Get the player controls visible"):
#             PlayerPage().player_window.double_click()
#             PlayerPage().player_window.hover()
#         with allure.step("Verify that the Volume button is in the Up state"):
#             PlayerPage().volume_button.should(have.attribute("class", "fa fa-volume-up"))
#             time.sleep(1)
#         with allure.step("Click on the Volume button"):
#             PlayerPage().volume_button.click()
#             time.sleep(1)
#         with allure.step("Verify that the Volume button is in the Off state"):
#             PlayerPage().volume_button.should(have.attribute("class", "fa fa-volume-off"))
#         with allure.step("Click on the Volume button"):
#             PlayerPage().volume_button.click()
#             time.sleep(1)
#         with allure.step("Verify that the Volume button is in the Up state"):
#             PlayerPage().volume_button.should(have.attribute("class", "fa fa-volume-up"))
#             time.sleep(3)
#             browser.quit_driver()
#
#
# @allure.title("Video Player: Volume slider verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Volume button, moves the slider and TBD               """)
# def test_player_volume_slider_verification():
#         with allure.step("Sign In as an existing user"):
#             SigninPage().login_as_user()
#             browser.quit_driver()
#         # Need to implement a step to drag and drop the Volume slider, TBD
#
#
# @allure.title("Video Player: Full Screen button verification")
# @allure.description("""The test opens video player from the Guide page, taps
# on the Full Screen button, then taps on it again and verifies that the playback is still on""")
# def test_player_full_screen_button_verification():
#         with allure.step("Sign In as an existing user"):
#             SigninPage().login_as_user()
#         with allure.step("Tap on the first channel in the list"):
#             GuidePage().first_channel_in_the_list.click()
#             time.sleep(9)
#         with allure.step("Get the player controls visible"):
#             PlayerPage().player_window.double_click()
#             PlayerPage().player_window.hover()
#         with allure.step("Click on the Full Screen button"):
#             PlayerPage().fullscreen_button.click()
#             time.sleep(1)
#         with allure.step("Verify that the Playback is still on"):
#             PlayerPage().playstop_stop_button.should(be.visible)
#             time.sleep(1)
#         with allure.step("Click on the Full Screen button again"):
#             PlayerPage().fullscreen_button.click()
#             time.sleep(1)
#         with allure.step("Verify that the Playback is still on"):
#             PlayerPage().playstop_stop_button.should(be.visible)
#             time.sleep(1)
#             browser.quit_driver()







