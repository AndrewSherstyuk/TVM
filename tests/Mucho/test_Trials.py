import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *

BASE_URL = "https://tvmucho.com/"

activationCode1 = "DDKE38"  # "brandnew121212@gmail.com"
activationCode2 = "8C5B9H"  # "brandnew1212@gmail.com"
activationCode3 = "53H4H1"  # "brandold1211@gmail.com"
activationCode4 = "KELB0H"  # "brandnew121213@gmail.com"
activationCode5 = "028974"  # "joel1976@mail.ru"

activation_codes_list = [activationCode1, activationCode2, activationCode3, activationCode4, activationCode5]



@allure.title("5 Min Trial: General verification")
@allure.description("""The test opens 5 Min trial mode and performs verification of that""")
def test_five_minutes_trial_playback():
        with allure.step("Open the 5 Min trial mode video playback"):
            browser.open_url(BASE_URL + "watch-tv-free/#live/bbc-one-hd")
            time.sleep(1)
        with allure.step("Verify that the circle is displayed and the text is 5 Min"):
            s("#time_probressbar").should(have.exact_text("5 min"))
        with allure.step("Verify that the Registration popup is displayed when it's called with a js function"):
            browser.execute_script("registrationAlert()")
            s("#registration-modal").should(be.visible)
        with allure.step("Verify that all the controls are available on the Registration popup"):
            s(by.xpath("(//BUTTON[@data-remodal-action='close'])[6]")).should(be.clickable)
            s(by.partial_link_text("Sign In")).should(be.clickable)
            s(by.xpath("//SPAN[@data-translate='pl_main_modal_reg_fb'][text()='Sign up with Facebook']")).should(be.clickable)
            s(by.xpath("//SPAN[@data-translate='pl_main_modal_reg_google'][text()='Sign up with Google']")).should(be.clickable)
            s(by.xpath("//A[@class='email button'][text()='SIGN UP WITH EMAIL']")).should(be.clickable)



@allure.title("60 Min Trial: General Verifiecation")
@allure.description("""The test logs in as the free registered user and verifies the !-hour Trial""")
def test_oops_1_hour_popup_verification_after_login():
    with allure.step("Open the Signin page of TVMucho"):
        browser.open_url(BASE_URL_2 + "watch-tv-free/activate/?showerror=true")
    with allure.step("Click on the Signin button on the popup"):
        SigninPage().sign_in_btn.click()
    with allure.step("Fill in the Code field with a valid Activation Code"):
        SigninPage().activation_code_field.set_value(activationCode1)
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
        time.sleep(110)
    with allure.step("Verify that the circle is displayed and the text is 5 Min"):
        s("#time_probressbar").should(have.exact_text("60 min"))
    with allure.step("Call the Share popup"):
        browser.execute_script("$('#share-modal').remodal().open()")
    with allure.step("Verify the Share popup"):
        shareModal = s("#share-modal")
        shareModal.should(be.visible)



    # with allure.step("Start playback of the first channel on the Channels list"):
    #     OneHourViewFlow().first_channel_in_the_scroller.click()
    #     time.sleep(2)
    # with allure.step("Verify that the playback is up and running"):
    #     OneHourViewFlow().player_playstop_button.should(be.visible)
    # with allure.step("Wait for 57.5 minutes"):
    #     time.sleep(3450)
    # with allure.step("Verify that the playback is up and running"):
    #     PlayerPage().player_window.click()
    # with allure.step("Wait for 5 minutes so the playback is expired"):
    #     time.sleep(300)
    # with allure.step("Verify that the Registration popup gets displayed"):
    #     OneHourViewFlow().oops_popup.should(be.visible)
    #     browser.quit_driver()

