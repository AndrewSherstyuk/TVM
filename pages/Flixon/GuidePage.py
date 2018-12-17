from selene.api import *


class GuidePage(object):

    def __init__(self):

        self.day_selector = s(".row.day-selector")

        self.first_channel_in_the_list = s(by.xpath('//*[@id="channel-selector"]/li[1]'))

        self.first_ongoing_program_in_epg = s(by.xpath("(//DIV[@class='epg-item current'])[1]"))

        self.first_ongoing_program_in_epg_custom_banner_arrow = s(by.xpath("(//SPAN[@class='icon icon-play'])[88]"))



    def select_the_1st_channel_in_the_list(self):
        self.first_channel_in_the_list.click()
        return


