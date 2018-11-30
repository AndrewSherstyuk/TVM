from selene.api import *


class MyTVPage(object):

    def __init__(self):
        self.row_schedule = s("#tv-guide-available")