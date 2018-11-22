from selene.api import *


class OnDemandPage(object):

    def __init__(self):
        self.categories_view = s("#categories-view")
        self.ondemand_1st_event = s(by.xpath("(//BUTTON[@class='item tv-guide-programme-item'])[1]"))
        self.ondemand_custom_banner_play_button = s(by.xpath("(//BUTTON[@class='item tv-guide-programme-item'])[1]/../../../..//BUTTON[@class='play item'][text()='Play now'][text()='Play now']"))

