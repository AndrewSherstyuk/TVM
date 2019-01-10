import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *
from pages.Flixon.OnNowPage import *
from pages.Flixon.OnDemandPage import *
from pages.Flixon.CinemaPage import *
from pages.Flixon.RecordingsPage import *
from pages.Flixon.MyTVPage import *
from pages.Flixon.SearchPage import *
from selene.conditions import *


@allure.title("Guide page: Play (arrow) button on the current program preview")
@allure.description("On the Guide page, the scripts clicks on a current event and verifies that there's the Play (arrow) button on the preview""")
def test_play_button_on_the_current_program_preview():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
        # with allure.step("Click Yes on the Personal Video Recording popup"):
        #     time.sleep(10)
        #     OneHourViewFlow().personal_video_recording_confirmation_button.click()
        #     time.sleep(2)
        # with allure.step("Click OK on the Hooray popup"):
        #     OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        #     time.sleep(2)
    with allure.step("Tap on the first channel in the list"):
        # GuidePage.first_last_available_program_in_epg.should(be.visible)
        # GuidePage().first_scheduled_program_in_epg_arrow_icon.should(be.visible)
        GuidePage().first_ongoing_program_in_epg.click()
        time.sleep(1)
        GuidePage().first_ongoing_program_in_epg_custom_banner_arrow.should(be.visible)
        browser.quit_driver()


@allure.title("Guide page: Record (circle) button on the scheduled program preview")
@allure.description("On the Guide page, the scripts clicks on a scheduled event and verifies that there's the Record (circle) button on the preview""")
def test_record_button_on_the_scheduled_program_preview():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
        # with allure.step("Click Yes on the Personal Video Recording popup"):
        #     time.sleep(10)
        #     OneHourViewFlow().personal_video_recording_confirmation_button.click()
        #     time.sleep(2)
        # with allure.step("Click OK on the Hooray popup"):
        #     OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        #     time.sleep(2)
    with allure.step("Tap on the first channel in the list"):
        # GuidePage.first_last_available_program_in_epg.should(be.visible)
        GuidePage().first_scheduled_program_in_epg.click()
        time.sleep(1)
        GuidePage().first_scheduled_program_in_epg_preview_record_button.should(be.visible)
        browser.quit_driver()


# @allure.title("Guide page: yellow arrows to indicate ongoing and recorded events")
# @allure.description(
#     "On the Guide page, the scripts checkes the ongoing and recorded events to see the yellow little arrow-shaped icon in the top right corn""")
# def test_back_button_right_after_login():
#     with allure.step("Sign In as an existing user"):
#         SigninPage().login_as_user()
#         time.sleep(5)

