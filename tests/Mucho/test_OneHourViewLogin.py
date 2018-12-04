import allure
from pages.Flixon.SigninPage import *
from pages.Mucho.OneHourViewFlow import *
from pages.Flixon.PlayerPage import *
from core.globals import *
from core.randomizer import *
import time


# email of the user = "brandnew121212@gmail.com"
activationCode1 = "DDKE38"
# email of the user = "brandnew1212@gmail.com"
activationCode2 = "8C5B9H"
# email of the user = "zv1py3@gmail.com"
activationCode3 = "GC56FJ"
# email of the user = "42ycqd@gmail.com"
activationCode5 = "C2801K"


@allure.title("")
@allure.description("""""")
def test_oops_1_hour_popup_verification_after_login():
    with allure.step("Open the Signin page of TVMucho"):
        browser.open_url(BASE_URL_2 + "watch-tv-free/activate/?showerror=true")
        time.sleep(10)
    with allure.step("Check if you're logged out. Log out if not"):
        try:
            PageHeader().log_out()
        except:
            pass
        time.sleep(5)
    with allure.step("Click on the Signin button on the popup"):
        SigninPage().sign_in_btn.click()
    with allure.step("Fill in the Code field with a valid Activation Code"):
        SigninPage().activation_code_field.set_value(activationCode5)
    with allure.step("Click on the Sign In button on the popup"):
        SigninPage().activation_code_signin_button.click()
        time.sleep(15)
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
        time.sleep(3450)
    with allure.step("Verify that the playback is up and running"):
        PlayerPage().player_window.click()
    with allure.step("Wait for 5 minutes so the playback is expired"):
        time.sleep(300)
    with allure.step("Verify that the Registration popup gets displayed"):
        OneHourViewFlow().oops_popup.should(be.visible)
        browser.quit_driver()




