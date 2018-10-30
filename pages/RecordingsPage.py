from selene.api import *


class RecordingsPage(object):

    def __init__(self):
        self.my_recordings_header = s(by.text("My recordings"))