import allure
from pages.Flixon.SigninPage import *
from pages.Flixon.PageHeader import *
from pages.Flixon.MyTVPage import *
from pages.Flixon.OnDemandPage import *
from pages.Flixon.RecordingsPage import *
from pages.Flixon.SearchPage import *

correct_email = "0000@0000.com"
correct_password = "010101"


@allure.title("Header navigation elements check")
@allure.description("""TC to check that all navigation buttons are presented""")
def test_navigation_elements():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Check that all header navigation buttons presented and visible"):
        PageHeader().cinema.should(be.visible)
        PageHeader().my_tv.should(be.visible)
        PageHeader().on_demand.should(be.visible)
        PageHeader().on_now.should(be.visible)
        PageHeader().recordings.should(be.visible)
        PageHeader().search.should(be.visible)
        browser.quit_driver()


@allure.title("Check that default active tab is Guide ")
@allure.description("""TC to check transitions between navigation tabs""")
def test_navigation_default_active_tab():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Check that default active tab is Guide"):
        assert PageHeader().guide.get_attribute("class") == "tab-toggle active"
        assert s(".tab-toggle.active").text == "GUIDE"
        browser.quit_driver()

@allure.title("Navigation to MyTV check ")
@allure.description("""TC to check transitions from Guide to MyTV""")
def test_navigation_to_mytv():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Navigate to MyTV"):
        PageHeader().my_tv.click()
    with allure.step("Check that page is opened"):
        MyTVPage().row_schedule.should(be.visible)
    with allure.step("Check active button + css styles"):
        assert PageHeader().guide.get_attribute("class") != "tab-toggle active"
        assert PageHeader().my_tv.get_attribute("class") == "tab-toggle active"
        assert s(".tab-toggle.active").text == "MY TV"
        browser.quit_driver()

@allure.title("Navigation to On Now check ")
@allure.description("""TC to check transitions from Guide to On Now""")
def test_navigation_to_on_now():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Navigate to On Now"):
        PageHeader().on_now.click()
    # with allure.step("Check that page is openned"):
    #     OnNowPage().heading.should(be.visible).should(be.clickable)
    with allure.step("Check active button + css styles"):
        assert PageHeader().guide.get_attribute("class") != "tab-toggle active"
        assert PageHeader().on_now.get_attribute("class") == "tab-toggle active"
        assert s(".tab-toggle.active").text == "ON NOW"
    browser.quit_driver()

@allure.title("Navigation to On Demand check ")
@allure.description("""TC to check transitions from Guide to On Demand""")
def test_navigation_to_on_demand():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Navigate to On Demand"):
        PageHeader().on_demand.click()
    with allure.step("Check that page is openned"):
        OnDemandPage().categories_view.should(be.visible).should(be.clickable)
    with allure.step("Check active button + css styles"):
        assert PageHeader().guide.get_attribute("class") != "tab-toggle dvr-content active"
        assert PageHeader().on_demand.get_attribute("class") == "tab-toggle dvr-content active"
        assert s(".tab-toggle.active").text == "ON DEMAND"
        browser.quit_driver()

@allure.title("Navigation to Cinema check ")
@allure.description("""TC to check transitions from Guide to Cinema""")
def test_navigation_to_cinema():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Navigate Cinema"):
        PageHeader().cinema.click()
    # with allure.step("Check that page is openned"):
    #     CinemaPage().drama_header.should(be.visible).should(be.clickable)
    with allure.step("Check active button + css styles"):
        assert PageHeader().guide.get_attribute("class") != "tab-toggle active"
        assert PageHeader().cinema.get_attribute("class") == "tab-toggle active"
        assert s(".tab-toggle.active").text == "CINEMA"
    browser.quit_driver()


@allure.title("Navigation to Recordings check ")
@allure.description("""TC to check transitions from Guide to Recordings""")
def test_navigation_recordings():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Navigate Recordings"):
        PageHeader().recordings.click()
    with allure.step("Check that page is openned"):
        RecordingsPage().my_recordings_header.should(be.visible).should(be.clickable)
    with allure.step("Check active button + css styles"):
        assert PageHeader().guide.get_attribute("class") != "tab-toggle active"
        assert PageHeader().recordings.get_attribute("class") == "tab-toggle active"
        assert s(".tab-toggle.active").text == "RECORDINGS"
        browser.quit_driver()


@allure.title("Navigation to Search check ")
@allure.description("""TC to check transitions from Guide to Recordings""")
def test_navigation_search():
    with allure.step("Login as existing user"):
        SigninPage().login_as_user()
    with allure.step("Navigate Recordings"):
        PageHeader().search.click()
    with allure.step("Check that page is openned"):
        SearchPage().search_input_field.should(be.visible).should(be.clickable)
    with allure.step("Check active button + css styles"):
        assert PageHeader().guide.get_attribute("class") != "tab-toggle active"
        assert PageHeader().search.get_attribute("class") == "tab-toggle active"
        assert s(".tab-toggle.active").text == "SEARCH"
        browser.quit_driver()









