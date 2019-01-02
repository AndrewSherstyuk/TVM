from pages.Flixon.GuidePage import *
from core.globals import *
import time
from pages.Flixon.PageHeader import *
from core.globals import *
from pages.Mucho.OneHourViewFlow import *


class SigninPage(object):

    correct_email = "0000@0000.com"
    correct_password = "010101"

    def __init__(self):
        self.logo = s("#logoimg")
        self.sign_in_btn = s("#suisi")
        self.welcome_text = s("#signupinwindow > div.signinheader")
        self.welcome_window = s("#signupinwindow")
        self.username_field = s("#username")
        self.password_field = s("#password")
        self.submit_login_btn = s('#signin')
        self.error_container = s(".login-error")
        self.error_message_text = s("Incorrect Username and/or Password")
        self.sign_in_header = s(".signinheader")

        self.activation_code_field = s("#activationcode")
        self.activation_code_signin_button = s("#signin")

        self.oops_popup = s("#activatewindow")
        self.oops_popup_retry_button = s("#retry")

    def tap_on_sign_in(self):
        # self.welcome_text.should(have.text('Welcome to Flixon TV...'))
        self.sign_in_btn.click()
        return

    def fill_in_the_username_field(self, email):
        self.username_field.set_value(email)

    def fill_in_the_password_field(self, password):
        self.password_field.set_value(password)

    def submit_login(self):
        self.submit_login_btn.click()

    def check_login_error_message(self):
        self.error_container.should(have.text("Incorrect Username and/or Password"))

    def check_that_signin_page_is_still_displayed(self):
        self.submit_login_btn.should(be.visible)

    def login_as_user(self):
        # try:
        #     browser.quit_driver()
        # except:
        #     pass
        browser.open_url(BASE_URL)
        time.sleep(5)
        try:
            PageHeader.log_out()
        except:
            pass
        SigninPage().tap_on_sign_in()
        SigninPage().fill_in_the_username_field(self.correct_email)
        SigninPage().fill_in_the_password_field(self.correct_password)
        SigninPage().submit_login()
        time.sleep(10)
        try:
            OneHourViewFlow().personal_video_recording_confirmation_button.click()
            time.sleep(2)
            OneHourViewFlow().personal_video_recording_hooray_ok_button.click()
            time.sleep(2)
        except:
            pass
        # GuidePage().day_selector.should(be.visible)






