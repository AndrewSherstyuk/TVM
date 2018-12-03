import allure
from pages.Mucho.OneHourViewFlow import *
from pages.Flixon.PlayerPage import *
from core.globals import *
from core.randomizer import *
import time


def wait_for_the_registration_modal():
    counter = 0
    result = False
    while result is not True:
        result = OneHourViewFlow().registration_modal.is_displayed()
        print(OneHourViewFlow().registration_modal.is_displayed())
        print(counter)
        time.sleep(5)
        counter += 1
        if counter == 60:
            raise Exception("1-min Continue Watching popup is not caught")



@allure.title("5 min popup verification")
@allure.description("""test test test test""")
def test_oops_1_hour_popup_verification():
    with allure.step("Open the Signin page of TVMucho"):
        browser.open_url(BASE_URL_2 + "watch-tv-free")
        time.sleep(5)
    with allure.step("Verify that the playback is in progress"):
        OneHourViewFlow().player_playstop_button.should(be.visible)
    with allure.step("Wait for the Registration Modal popup"):
        wait_for_the_registration_modal()
    with allure.step("Click on the Cross button to close the Registration Modal"):
        OneHourViewFlow().five_min_popup_close_button.should(be.visible)
        time.sleep(1)
        OneHourViewFlow().five_min_popup_close_button.click()
    with allure.step("Wait for the Registration modal popup"):
        wait_for_the_registration_modal()
    with allure.step("Click on the Cross button to close the Registration Modal"):
        OneHourViewFlow().five_min_popup_close_button.should(be.visible)
        time.sleep(1)
        OneHourViewFlow().five_min_popup_close_button.click()
    # with allure.step("Verify that the playback is in progress after the popup gets closed"):
    #     PlayerPage().player_window.click()
    #     time.sleep(1)
    #     PlayerPage().playstop_stop_button.should(be.visible)
    with allure.step("Wait for the Registration modal popup"):
        wait_for_the_registration_modal()
        print("SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP ")
        time.sleep(30)
    with allure.step("Click on the Cross button to close the Registration Modal"):
        OneHourViewFlow().five_min_popup_close_button.should_not(be.visible)
        time.sleep(1)

