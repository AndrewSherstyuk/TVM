import allure
from pages.Mucho.TrialsObj import *
from pages.Flixon.SigninPage import *

BASE_URL = "https://tvmucho.com/"

activationCode1 = "9E1L2C"  # "brandnew121212@gmail.com"   http://tvmucho.com/player/?activationcode=9E1L2C
activationCode2 = "AE9C11"  # "brandnew1212@gmail.com"   http://tvmucho.com/player/?activationcode=AE9C11
activationCode3 = "BA5419"  # "brandold1211@gmail.com"   http://tvmucho.com/player/?activationcode=BA5419
activationCode4 = "5H7HKB"  # "brandnew121213@gmail.com"   http://tvmucho.com/player/?activationcode=5H7HKB
activationCode5 = "8KGJ7D"  # "joel1976@mail.ru"   http://tvmucho.com/player/?activationcode=8KGJ7D
activationCode6 = "D92A4E"  # "andreys@reali.com   http://tvmucho.com/player/?activationcode=D92A4E

activation_codes_list = [activationCode1, activationCode2, activationCode3, activationCode4, activationCode5]



@allure.title("5 Min Trial: General verification")
@allure.description("""The test opens 5 Min trial mode and performs verification of that""")
def test_five_minutes_trial_playback():
        with allure.step("Open the 5 Min trial mode video playback"):
            browser.open_url(BASE_URL + "watch-tv-free/#live/bbc-one-hd")
            time.sleep(1)
        with allure.step("Perform the general verification of the player controls (ongoing event)"):
            PlayerPage_5MinTrial().initial_check_of_player_page_ongoing_event()
            time.sleep(60)
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



# @allure.title("60 Min Trial: General Verifiecation")
# @allure.description("""The test logs in as the free registered user and verifies the 1-hour Trial functionality""")
# def test_oops_1_hour_popup_verification_after_login():
#     with allure.step("Open My TV page with direct link"):
#         browser.open_url(BASE_URL + "player/?activationcode=" + activationCode2)
#         time.sleep(1)
#         try:
#             oopsTooManyAccountsPopup = s(by.partial_link_text("Or force all my devices to stop playing."))
#             if oopsTooManyAccountsPopup.is_displayed() is True:
#                 oopsTooManyAccountsPopup.click()
#         except:
#             pass
#     with allure.step("Launch the ongoing video playback"):
#         browser.open_url(BASE_URL + "watch-tv-free/#live/bbc-one-hd")
#         time.sleep(1)
#     with allure.step("Verify that the circle is displayed and the text is 60 Min"):
#         s("#time_probressbar").should(have.exact_text("59 min"))
#     with allure.step("Wait for the player control to fade away"):
#         time.sleep(7)
#     with allure.step("Verify that the time circle disappears along with player controls"):
#         s("#time_probressbar").should_not(be.visible)
#     with allure.step("Make the player controls visible again"):
#         s("#player").click()
#     with allure.step("Verify that the time circle appears as soon as the player controls get visible again"):
#         s("#time_probressbar").should(be.visible)
#     with allure.step("Call the Share popup ensure it has appeared"):
#         browser.execute_script("$('#share-modal').remodal().open()")
#         s("#share-modal").should(be.visible)
#     with allure.step("Call the Fire event and ensure it has appeared"):
#         browser.execute_script("fireEvent('apiError', 'free_time_over')")
#         s("#content > div.main-content > div.form.first").should(be.visible)






