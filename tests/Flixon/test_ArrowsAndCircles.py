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


@allure.title("Guide page: yellow arrows to indicate ongoing and recorded events")
@allure.description("On the Guide page, the scripts checkes the ongoing and recorded events to see the yellow little arrow-shaped icon in the top right corn""")
def test_back_button_right_after_login():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
        time.sleep(5)


@allure.title("Guide page: yellow arrows to indicate ongoing and recorded events")
@allure.description("On the Guide page, the scripts checkes the ongoing and recorded events to see the yellow little arrow-shaped icon in the top right corn""")
def test_back_button_right_after_login():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
        time.sleep(5)


@allure.title("Guide page: yellow arrows to indicate ongoing and recorded events")
@allure.description(
    "On the Guide page, the scripts checkes the ongoing and recorded events to see the yellow little arrow-shaped icon in the top right corn""")
def test_back_button_right_after_login():
    with allure.step("Sign In as an existing user"):
        SigninPage().login_as_user()
        time.sleep(5)

