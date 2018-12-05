from selene.api import *


class OnNowPage(object):

    def __init__(self):
        self.heading = s('.heading[1]')
        self.on_now_1st_event = s(by.xpath("(//DIV[@class='content'])[1]"))
        self.channels_table = s("#channels")