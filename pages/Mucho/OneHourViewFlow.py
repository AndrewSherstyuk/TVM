from selene.api import *

class OneHourViewFlow(object):

    def __init__(self):

        # /registration-1hour

        # 1st screen
        self.continue_watching_popup_title = s(by.partial_text("Continue watching?"))
        self.sign_in_button = s(by.text("Sign In"))
        self.log_in_with_facebook = s(by.text("Log in with Facebook"))
        self.log_in_with_google = s(by.text("Log in with Google"))
        self.log_in_with_email_button = s("#content > div.main-content > div.form.first > button.goto")

        # /watch-tv/activate
        self.oops_popup_title = s(by.text("Oops..."))
        self.renew_button = s("#renew")
        self.retry_button = s("#retry")
        self.get_help_button = s(by.text("Get Help"))
        self.sign_up_now_button = s(by.text("Sign up now"))
        self.email = s(by.partial_link_text("support@tvmucho.com"))

        # 1 Hour A Day For Free popup
        self.title = s(by.partial_text("1 hour a day for Free!"))
        self.name_field = s("#content > div.main-content > div.form.sign-up > input.name")
        self.email_field = s("#content > div.main-content > div.form.sign-up > input.email.keypress-hook")
        self.continue_button = s(".hook.continue")

        # Congratulations popup
        self.congratulations_title = s(by.text("Congratulations!"))
        self.congratulations_start_watching_online_button = s("#content > div.main-content > div.form.congratulations > a")
        self.help_email_button = s(by.partial_link_text("support@tvmucho.com"))


        # /watch-tv screen

        # personalvideo_recording_popup
        self.personalvideo_recording_popup_title = s("#modal1")
        self.personalvideo_recording_popup_title_text = s(by.text("Personal Video Recording"))
        self.no_button_on_video_recording_popup = s("#cancel1")
        # hooray popup
        self.yes_button_on_video_recording_popup = s("#confirm1")
        self.hooray_popup = s("#modal2")
        self.ok_button_on_hooray_popup = s("#confirm2")

        self.first_channel_in_the_scroller = s(by.xpath('//*[@id="channels"]/div[4]/div[1]/button[1]'))
        self.player_playstop_button = s("#playstop")

        # Registration Modal
        self.registration_modal = s("#registration-modal")
        self.registration_modal_signup_with_email_button = s("#registration-modal > button.email.login.button")
        self.yourname_field = s("#email-modal > div:nth-child(4) > input")
        self.youremail_field = s("#email-modal > div:nth-child(5) > input")
        self.another_continue_button = s("#email-modal > div:nth-child(7) > button > span.text")
        self.congratulations_modal_continue_button = s("#congratulations-modal > button.button")

        # Personal Video Recording
        self.personal_video_recording_confirmation_button = s("#confirm1")
        self.personal_video_recording_hooray_ok_button = s("#confirm2")

        # "Oops... You have reached your time limit for today" popup
        self.oops_popup = s("#activate")



















