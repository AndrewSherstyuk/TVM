from selene.api import *


class GuidePage(object):

    def __init__(self):

        self.day_selector = s(".ui-selectmenu-text")

        self.first_channel_in_the_list = s(by.xpath('//*[@id="channel-selector"]/li[1]'))

    def select_the_1st_channel_in_the_list(self):
        self.first_channel_in_the_list.click()
        return
