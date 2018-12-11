import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *






@allure.title("Video Player: Play/Stop button verification")
@allure.description("""The test opens video player from the Guide page, taps
        on the Playstop button and verifies its Stop and Play states""")
def test_player_playstop_button_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Verify that the Playstop button is still in the stop state"):
            PlayerPage().playstop_stop_button.should(be.visible)
        with allure.step("Click on the Playstop button"):
            PlayerPage().playstop_stop_button.click()
            time.sleep(1)
        with allure.step("Verify that the Playstop button is in the Play state"):
            PlayerPage().playstop_play_button.should(be.visible)
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
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the CC button"):
            PlayerPage().cc_menu_button.click()
        with allure.step("Select the English option from the CC menu"):
            try:
                PlayerPage().cc_menu_english_option.click()
            except:
                pass


        #     # Here we need to check that the subtitles are actually visible

        with allure.step("Click on the CC button"):
            PlayerPage().cc_menu_button.click()
        with allure.step("Select the Off option from the CC menu"):
            PlayerPage().cc_menu_off_option.click()

        #     # Here we need to check that the subtitles are not displayed any longer

            browser.quit_driver()




@allure.title("Video Player: Volume button verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Volume button, TBD               """)
def test_player_volume_button_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
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


@allure.title("Video Player: Volume slider verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Volume button, moves the slider and TBD               """)
def test_player_volume_slider_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
            browser.quit_driver()
        # Need to implement a step to drag and drop the Volume slider, TBD


@allure.title("Video Player: Full Screen button verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Full Screen button, then taps on it again and verifies that the playback is still on""")
def test_player_full_screen_button_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
            time.sleep(9)
        with allure.step("Get the player controls visible"):
            PlayerPage().player_window.double_click()
            PlayerPage().player_window.hover()
        with allure.step("Click on the Full Screen button"):
            PlayerPage().fullscreen_button.click()
            time.sleep(1)
        with allure.step("Verify that the Playback is still on"):
            PlayerPage().playstop_stop_button.should(be.visible)
            time.sleep(1)
        with allure.step("Click on the Full Screen button again"):
            PlayerPage().fullscreen_button.click()
            time.sleep(1)
        with allure.step("Verify that the Playback is still on"):
            PlayerPage().playstop_stop_button.should(be.visible)
            time.sleep(1)
            browser.quit_driver()







