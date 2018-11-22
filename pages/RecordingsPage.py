from selene.api import *


class RecordingsPage(object):

    def __init__(self):
        self.my_recordings_header = s(by.text("My recordings"))
        self.recording_page_first_existing_recording = s(by.xpath("(//DIV[@class='duration'][text()='recorded'][text()='recorded'])[1]"))