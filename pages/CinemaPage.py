from selene.api import *


class CinemaPage(object):

    def __init__(self):
        self.drama_header = s('#vod-view > div:nth-child(3) > div.heading')
        self.cinema_page_1st_event = s(by.xpath("(//BUTTON[@class='item poster'])[1]"))
        self.cinema_page_custom_banner_play_button = s(by.xpath("//BUTTON[@class='play item play-vod'][text()='PLAY NOW']"))


