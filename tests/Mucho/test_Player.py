import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *





@allure.title("Video Player: Volume button verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Volume button, TBD               """)
def test_player_volume_button_verification():
        # with allure.step("Sign In as an existing user"):
        #     SigninPage().login_as_user()

        with allure.step("Sign in"):
            SigninPage().login_as_user_tvmucho()
            time.sleep(10)
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_scroller.should(be.visible)
            GuidePage().first_channel_in_the_scroller.should(be.clickable)
            GuidePage().first_channel_in_the_scroller.click()
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.click()
            # PlayerPage().player_window.hover()
        with allure.step("Verify that the Volume button is in the Up state"):
            PlayerPage().volume_button.should(have.attribute("class", "fa fa-volume-up"))
            time.sleep(1)
        with allure.step("Click on the Volume button"):
            PlayerPage().volume_button.click()
            time.sleep(1)
        with allure.step("Verify that the Volume button is in the Off state"):
            PlayerPage().volume_button.should(have.attribute("class", "fa fa-volume-off"))
        with allure.step("Click on the Volume button"):
            PlayerPage().volume_button.click()
            time.sleep(1)
        with allure.step("Verify that the Volume button is in the Up state"):
            PlayerPage().volume_button.should(have.attribute("class", "fa fa-volume-up"))
            time.sleep(3)
            browser.quit_driver()