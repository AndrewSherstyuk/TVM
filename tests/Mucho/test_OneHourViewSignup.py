import allure
from pages.Mucho.OneHourViewFlow import *
from pages.Flixon.PlayerPage import *
from core.globals import *
from core.randomizer import *
import time



@allure.title("")
@allure.description("""""")
def test_oops_1_hour_popup_verification():
    with allure.step("Open the Signin page of TVMucho"):
        browser.open_url(BASE_URL_2 + "registration-1hour/")
    with allure.step("Click on the Log In With Email button on the popup"):
        OneHourViewFlow().log_in_with_email_button.click()
    with allure.step("Fill in the Name field with a randomly generated name"):
        OneHourViewFlow().name_field.set_value(Randomizer.word())
    with allure.step("Fill in the Name field with a randomly generated email"):
        OneHourViewFlow().email_field.set_value(Randomizer.email())
    with allure.step("Click on the Continue button on the popup"):
        OneHourViewFlow().continue_button.click()
        time.sleep(4)
    with allure.step("Click Start Watching Online button on the Congratulations popup"):
        OneHourViewFlow().congratulations_start_watching_online_button.click()
        time.sleep(3)
    with allure.step("Verify that the playback is in progress"):
        OneHourViewFlow().player_playstop_button.should(be.visible)
    with allure.step("Wait for the Registration Modal popup"):
        counter = 0
        result = False
        while result is not True:
            result = OneHourViewFlow().registration_modal.is_displayed()
            print(OneHourViewFlow().registration_modal.is_displayed())
            print(counter)
            time.sleep(10)
            counter += 1
            if counter == 65:
                raise Exception("1-min Continue Watching popup is not caught")
    with allure.step("Click on the Sign In with Email button on the Registration Modal"):
        OneHourViewFlow().registration_modal_signup_with_email_button.click()
        time.sleep(1)
        if OneHourViewFlow().registration_modal_signup_with_email_button.is_displayed():
            OneHourViewFlow().registration_modal_signup_with_email_button.click()
    with allure.step("Fill in Your Name field with a randomly generated username"):
        OneHourViewFlow().yourname_field.set_value(Randomizer.word())
    with allure.step("Fill in Your Email field with a randomly generated email"):
        OneHourViewFlow().youremail_field.set_value(Randomizer.email())
    with allure.step("Submit the form"):
        OneHourViewFlow().another_continue_button.click()
        time.sleep(3)
    with allure.step("Click on the Continue button on the Congratulations screen"):
        OneHourViewFlow().congratulations_modal_continue_button.click()
    with allure.step("Wait for the Personal Video Recording popup"):
        time.sleep(30)
    with allure.step("Click Yes on the Personal Video Recording popup"):
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(10)
    with allure.step("Start playback of the first channel on the Channels list"):
        OneHourViewFlow().first_channel_in_the_scroller.click()
        time.sleep(2)
    with allure.step("Verify that the playback is up and running"):
        OneHourViewFlow().player_playstop_button.should(be.visible)
    with allure.step("Wait for 57.5 minutes"):
        time.sleep(3400)
    with allure.step("Verify that the playback is up and running"):
        PlayerPage().player_window.click()
        OneHourViewFlow().player_playstop_button.should(be.visible)
        time.sleep(2)
    with allure.step("Wait for 5 minutes so the playback is expired"):
        time.sleep(300)
    with allure.step("Verify that the Registration popup gets displayed"):
        OneHourViewFlow().oops_popup.should(be.visible)
        browser.quit_driver()




