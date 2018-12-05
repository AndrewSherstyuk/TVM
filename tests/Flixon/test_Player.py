import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *




@allure.title("Video Player: Initial state of the page verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Home button and verifies that the Guide screen opens""")
def test_player_initial_state_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(2)
    # with allure.step("Get the player controls visible"):
    #     PlayerPage().player_window.double_click()
    #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of the page"):
        PlayerPage().initial_check_of_player_page_ongoing_event()
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Home button verification")
@allure.description("""The test opens video player from the Guide page, taps
on the Home button and verifies that the Guide screen opens""")
def test_player_home_button_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Tap on the Home button"):
        PlayerPage().tap_on_home_button()
        time.sleep(1)
    with allure.step("Verify that the Guide page is opened"):
        GuidePage().day_selector.should(be.visible)
        browser.quit_driver()


@allure.title("Video Player: Channels button verification")
@allure.description(
    """The test opens video player, taps on the Channels button and verifies that the Channels list gets visible.""")
def test_player_channels_button_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Tap on the Channels button"):
        PlayerPage().tap_on_channels_button()
    with allure.step("Verify that the channels line got visible"):
        PlayerPage().channels_left_arrow_button.should(be.visible)
        PlayerPage().channels_right_arrow_button.should(be.visible)
    with allure.step("Wait for the Player controls to get hidden"):
        time.sleep(10)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Verify that the Channels List is not displayed any longer"):
        PlayerPage().channels_button.should(be.visible)
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Favourite button verification")
@allure.description("""The test opens video player from the Guide page, taps
    on the Favourite button and verifies its selected and unselected states""")
def test_player_favourite_button_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
    with allure.step("Verify that the Favourite button is not clicked"):
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart-o'))
    with allure.step("Wait for the Player controls to disappear"):
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Verify that the Favourite button is still not clicked"):
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart-o'))
    with allure.step("Click on the Favourite button"):
        PlayerPage().favorite_button.click()
    with allure.step("Verify that the Favourite button is clicked"):
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart'))
    with allure.step("Click on the Favourite button again to make the event not favourite again"):
        PlayerPage().favorite_button.click()
        PlayerPage().favorite_button.should(have.attribute('class', 'fa fa-heart-o'))
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Play/Stop button verification")
@allure.description("""The test opens video player from the Guide page, taps
        on the Playstop button and verifies its Stop and Play states""")
def test_player_playstop_button_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
        with allure.step("Verify that the Playstop button is in the Stop state"):
            PlayerPage().playstop_stop_button.should(be.visible)
            time.sleep(2)
        # with allure.step("Wait for the Player controls to disappear"):
        #     time.sleep(9)
        # with allure.step("Get the player controls visible"):
        #     PlayerPage().player_window.double_click()
        #     PlayerPage().player_window.hover()
        # with allure.step("Verify that the Playstop button is still in the stop state"):
        #     PlayerPage().playstop_stop_button.should(be.visible)
        with allure.step("Click on the Playstop button"):
            PlayerPage().playstop_stop_button.click()
        with allure.step("Verify that the Playstop button is in the Play state"):
            PlayerPage().playstop_play_button.should(be.visible)
        with allure.step("Click on the Playstop button again to verify that it's in Stop state again"):
            PlayerPage().playstop_play_button.click()
            PlayerPage().playstop_stop_button.should(be.visible)
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
            time.sleep(2)
        # with allure.step("Wait for the Player controls to disappear"):
        #     time.sleep(9)
        # with allure.step("Get the player controls visible"):
        #     PlayerPage().player_window.double_click()
        #     PlayerPage().player_window.hover()
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
            time.sleep(2)
        # with allure.step("Wait for the Player controls to disappear"):
        #     time.sleep(9)
        # with allure.step("Get the player controls visible"):
        #     PlayerPage().player_window.double_click()
        #     PlayerPage().player_window.hover()
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
on the Full Screen button, TBD               """)
def test_player_fullscreen_button_verification():
        with allure.step("Sign In as an existing user"):
            SigninPage().login_as_user()
        with allure.step("Tap on the first channel in the list"):
            GuidePage().first_channel_in_the_list.click()
            time.sleep(2)
        # with allure.step("Wait for the Player controls to disappear"):
        #     time.sleep(9)
        # with allure.step("Get the player controls visible"):
        #     PlayerPage().player_window.double_click()
        #     PlayerPage().player_window.hover()
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







