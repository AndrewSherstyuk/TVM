from selene.api import *
import time

BASE_URL = "http://flixon.tvmucho.com"
BASE_URL_2 = "https://tvmucho.com/"
# BASE_URL = "http://flixon.tvmucho.com"


class Globals(object):

    def __init__(self):

        # personal video_recording_popup
        self.personalvideo_recording_popup_title = s("#modal1")
        self.personalvideo_recording_popup_title_text = s(by.text("Personal Video Recording"))
        self.no_button_on_video_recording_popup = s("#cancel1")
        self.yes_button_on_video_recording_popup = s("#confirm1")
        # hooray popup showing up after the personal recording video popup confirmed
        self.hooray_popup = s("#modal2")
        self.ok_button_on_hooray_popup = s("#confirm2")

    def confirm_the_personal_recording_popup(self):
        self.yes_button_on_video_recording_popup.click()
        time.sleep(2)
        self.ok_button_on_hooray_popup.click()
        time.sleep(2)