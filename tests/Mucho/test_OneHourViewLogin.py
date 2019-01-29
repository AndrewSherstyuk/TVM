import allure
from pages.Flixon.SigninPage import *
from pages.Mucho.OneHourViewFlow import *
from pages.Flixon.PlayerPage import *
from core.globals import *
from core.randomizer import *
import time



activationCode1 = "DDKE38" # "brandnew121212@gmail.com"
activationCode2 = "8C5B9H" # "brandnew1212@gmail.com"
activationCode3 = "9AK7C6" # "brandold1211@gmail.com"
activationCode4 = "KELB0H" # "brandnew121213@gmail.com"
activationCode5 = "028974" # "joel1976@mail.ru"

activation_codes_list = [activationCode1, activationCode2, activationCode3, activationCode4, activationCode5]



@allure.title("")
@allure.description("""""")
def test_oops_1_hour_popup_verification_after_login():
    with allure.step("Open the Signin page of TVMucho"):
        browser.open_url(BASE_URL_2 + "watch-tv-free/activate/?showerror=true")
    with allure.step("Click on the Signin button on the popup"):
        SigninPage().sign_in_btn.click()
    with allure.step("Fill in the Code field with a valid Activation Code"):
        SigninPage().activation_code_field.set_value(activationCode4)
    with allure.step("Click on the Sign In button on the popup"):
        SigninPage().activation_code_signin_button.click()
        for activation_code in activation_codes_list:
            try:
                if SigninPage().oops_popup.is_displayed() is True:
                    browser.open_url(BASE_URL_2 + "watch-tv-free/activate/?showerror=true")
                    SigninPage().sign_in_btn.click()
                    time.sleep(1)
                    SigninPage().activation_code_field.set_value(activation_code)
                    print(activation_code)
                    SigninPage().activation_code_signin_button.click()
                    time.sleep(1)
                else:
                    break
            except:
                pass
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




