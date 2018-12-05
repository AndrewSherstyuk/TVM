import allure
from pages.Flixon.PlayerPage import *
from pages.Flixon.SigninPage import *
from pages.Flixon.OnNowPage import *
from pages.Flixon.OnDemandPage import *
from pages.Flixon.CinemaPage import *
from pages.Flixon.RecordingsPage import *
from pages.Flixon.MyTVPage import *
from pages.Flixon.SearchPage import *
from selene.conditions import *


@allure.title("Back button: If clicked right after the login, then it closes the site")
@allure.description("The test opens the sites, logs in and clicks the Back button as soon as "
"gets to the Guide page right after having got logged in")
def test_back_button_right_after_login():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
        time.sleep(5)
        GuidePage().day_selector.should(be.visible)
        UrlContaining("/#guide")
    with allure.step("Press on the Back button"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
    with allure.step("Verify that you're on the Guide screen"):
        GuidePage().day_selector.should(be.visible)
        UrlContaining("/#guide")

@allure.title("Main Navigation: Back button functioning verification")
@allure.description("""The test opens the site and moves through all the tab of the main navigation.
Then it moves back step by step and verifies that the tabs are getting opened in inverted order""")
def test_back_button_functioning_through_main_nav():

    # Move forward

    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
        time.sleep(5)
        GuidePage().day_selector.should(be.visible)
        UrlContaining("/#guide")
    with allure.step("Move to My TV page and verify you're there"):
        PageHeader().my_tv.click()
        time.sleep(5)
        MyTVPage().row_schedule.should(be.visible)
        UrlContaining("/#home")
    with allure.step("Move to On Now page and verify you're there"):
        PageHeader().on_now.click()
        time.sleep(5)
        OnNowPage().channels_table.should(be.visible)
        UrlContaining("/#live-channels")
    with allure.step("Move to On Demand page and verify you're there"):
        PageHeader().on_demand.click()
        time.sleep(5)
        OnDemandPage().categories_view.should(be.visible)
        UrlContaining("/#on-demand")
    with allure.step("Move to the Cinema page and verify you're there"):
        PageHeader().cinema.click()
        time.sleep(5)

        UrlContaining("/#cinema")
    with allure.step("Move to the Recordings page and verify you're there"):
        PageHeader().recordings.click()
        time.sleep(5)

        UrlContaining("/#recordings")
    with allure.step("Move to the Search page and verify you're there"):
        PageHeader().search.click()
        time.sleep(5)
        SearchPage().search_input_field.should(be.visible)
        UrlContaining("/#search")
    with allure.step("Move to the Guide page and verify you're there"):
        PageHeader().guide.click()
        time.sleep(5)
        GuidePage().day_selector.should(be.visible)
        UrlContaining("/#guide")

        # Move back

    with allure.step("Make one step back to the Search page and verify you're there"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
        SearchPage().search_input_field.should(be.visible)
        UrlContaining("/#search")
    with allure.step("Make one step back to the Recordings page and verify you're there"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)

        UrlContaining("/#recordings")
    with allure.step("Make one step back to the Cinema page and verify you're there"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)

        UrlContaining("/#cinema")
    with allure.step("Make one step back to On Demand page and verify you're there"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
        OnDemandPage().categories_view.should(be.visible)
        UrlContaining("/#on-demand")
    with allure.step("Make one step back to the On Now page and verify you're there"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
        OnNowPage().channels_table.should(be.visible)
        UrlContaining("/#live-channels")
    with allure.step("Make one step back to My TV page and verify you're there"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
        MyTVPage().row_schedule.should(be.visible)
        UrlContaining("/#home")
    with allure.step("Make one step back to the Guide page and verify you're there"):
        browser.execute_script("history.back(-1)")
        time.sleep(5)
        GuidePage().day_selector.should(be.visible)
        UrlContaining("/#guide")