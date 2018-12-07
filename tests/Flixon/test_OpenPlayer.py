import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *
from pages.Flixon.OnNowPage import *
from pages.Flixon.OnDemandPage import *
from pages.Flixon.CinemaPage import *
from pages.Flixon.RecordingsPage import *
from pages.Flixon.SearchPage import *
from selene.conditions import *
from pages.Mucho.OneHourViewFlow import *


@allure.title("Video Player: Open from My TV page + Initial state of the player verification")
@allure.description("""The test opens video player from the My TV page and verifies that the player
 contains all the controls and those are up and running""")
def test_player_from_mytv_initial_state_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Navigate to On Now page"):
        PageHeader().my_tv.click()
    with allure.step("Open the 1st event on On Now page"):
        OnNowPage().on_now_1st_event.click()
        time.sleep(9)
    with allure.step("Get the player controls visible"):
        PlayerPage().player_window.double_click()
        PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of the page"):
        PlayerPage().initial_check_of_player_page()
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Open from On Now page + Initial state of the player verification")
@allure.description("""The test opens video player from the On Now page and verifies that the player
contains all the controls and those are up and running""")
def test_player_from_on_now_initial_state_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Navigate to On Now page"):
        PageHeader().on_now.click()
    with allure.step("Open the 1st event on On Now page"):
        OnNowPage().on_now_1st_event.click()
        time.sleep(2)
    # with allure.step("Get the player controls visible"):
    #     PlayerPage().player_window.double_click()
    #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of the page"):
        PlayerPage().initial_check_of_player_page_ongoing_event()
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the On Now page"):
        OnNowPage().channels_table.should(be.visible)
        UrlContaining("/#live-channels")
        browser.quit_driver()


@allure.title("Video Player: Open from On Demand page + Initial state of the player verification")
@allure.description("""The test opens video player from the On Demand page and verifies that the player
contains all the controls and those are up and running""")
def test_player_from_ondemand_initial_state_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Navigate to On Now page"):
        PageHeader().on_demand.click()
    with allure.step("Open the banner for the 1st event on On Now page"):
        OnDemandPage().ondemand_1st_event.click()
        time.sleep(1)
    with allure.step("Click on the Play button on the custom banner opened for the 1st event on the page"):
        OnDemandPage().ondemand_custom_banner_play_button.click()
        time.sleep(2)
    # with allure.step("Get the player controls visible"):
    #     PlayerPage().player_window.double_click()
    #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of the page"):
        PlayerPage().initial_check_of_player_page_recorded_event()
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the On Demand page"):
        OnDemandPage().categories_view.should(be.visible)
        UrlContaining("/#on-demand")
        browser.quit_driver()


@allure.title("Video Player: Open from Cinema page + Initial state of the player verification")
@allure.description("""The test opens video player from the Cinama page and verifies that the player
contains all the controls and those are up and running, recorded stream""")
def test_player_from_Guide_initial_state_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Navigate to Cinema page"):
        PageHeader().cinema.click()
    with allure.step("Open the banner for the 1st event on Cinema page"):
        CinemaPage().cinema_page_1st_event.click()
        time.sleep(1)
    with allure.step("Click on the Play button on the custom banner opened for the 1st event on the page"):
        CinemaPage().cinema_page_custom_banner_play_button.click()
        time.sleep(5)
    # with allure.step("Get the player controls visible"):
    #     PlayerPage().player_window.double_click()
    #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of a recorded event"):
        PlayerPage().initial_check_of_player_page_recorded_event()
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the Cinema page again"):
        UrlContaining("/#cinema")
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Open from Guide page, first channel in the list + Initial state of the player verification")
@allure.description("""The test opens video player from the Guide page, first channel in the left list, and verifies that the player
contains all the controls and those are up and running, ongoing player""")
def test_player_from_guide_initial_state_verification_1():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_channel_in_the_list.click()
        time.sleep(2)
        # with allure.step("Get the player controls visible"):
        #     PlayerPage().player_window.double_click()
        #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of the page"):
        PlayerPage().initial_check_of_player_page_ongoing_event()
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the Guide page again"):
        GuidePage().day_selector.should(be.visible)
        UrlContaining("/#guide")
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Open from Guide page, then open the first "
              "ongoing event from the Guide + Initial state of the player verification")
@allure.description("""The test opens video player from the Guide page, ongoing event from the guide, and verifies that the player
contains all the controls and those are up and running, ongoing player""")
def test_player_from_guide_initial_state_verification_2():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Tap on the first channel in the list"):
        GuidePage().first_ongoing_program_in_epg.click()
        GuidePage().first_ongoing_program_in_epg_custom_banner_arrow.click()
    # with allure.step("Get the player controls visible"):
    #     PlayerPage().player_window.double_click()
    #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of the page"):
        PlayerPage().initial_check_of_player_page_ongoing_event()
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the Guide page again"):
        GuidePage().day_selector.should(be.visible)
        UrlContaining("/#guide")
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Open from Recordings page + Initial state of the player verification")
@allure.description("""The test opens video player from the Recordings page and verifies that the player
contains all the controls and those are up and running, recorded stream""")
def test_player_from_recordings_initial_state_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Navigate to Recordings page"):
        PageHeader().recordings.click()
    with allure.step("Open the banner for the 1st event on Cinema page"):
        RecordingsPage().recording_page_first_existing_recording.click()
        time.sleep(2)
    # with allure.step("Get the player controls visible"):
    #     PlayerPage().player_window.double_click()
    #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of a recorded event"):
        PlayerPage().initial_check_of_player_page_recorded_event()
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the Recordings page again"):

        UrlContaining("/#recordings")
        time.sleep(1)
        browser.quit_driver()


@allure.title("Video Player: Open from the Search page + Initial state of the player verification")
@allure.description("""The test opens video player from the Search page and verifies that the player
contains all the controls and those are up and running, recorded stream""")
def test_player_from_search_initial_state_verification():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
    with allure.step("Click Yes on the Personal Video Recording popup"):
        time.sleep(10)
        OneHourViewFlow().personal_video_recording_confirmation_button.click()
        time.sleep(2)
    with allure.step("Click OK on the Hooray popup"):
        OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
        time.sleep(2)
    with allure.step("Navigate to Search page"):
        PageHeader().search.click()
        time.sleep(1)
    with allure.step("Set 'Cold Squad' as the Search criterion"):
        SearchPage().search_input_field.set_value("Cold Squad")
        time.sleep(5)
    with allure.step("Click on the 'Cold Squad' title on the found event"):
        SearchPage().cold_squad_found_event.click()
        time.sleep(2)
    with allure.step("Select the 1st season from the preview"):
        SearchPage().cold_squad_first_season_select.click()
    with allure.step("Select the 1st episode of the 1st season of the movie"):
        SearchPage().cold_squad_first_season_first_episode_select.click()
        time.sleep(2)
    with allure.step("Click on the Play button on the preview for the 1st season, 1st episode of Cold Squad"):
        SearchPage().cold_squad_first_season_first_episode_preview_play_button.click()
        time.sleep(2)
    # with allure.step("Get the player controls visible"):
    #     PlayerPage().player_window.double_click()
    #     PlayerPage().player_window.hover()
    with allure.step("Verify the initial state of a recorded event"):
        PlayerPage().initial_check_of_player_page_recorded_event()
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the Search page again"):
        SearchPage().search_input_field.should(be.visible)
        UrlContaining("/#search")
        time.sleep(1)
        browser.quit_driver()