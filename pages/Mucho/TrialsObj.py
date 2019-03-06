from selene.api import *




class PlayerPage_5MinTrial(object):

    def __init__(self):

        # 5 Min Trial Player controls that should be enabled
        self.home_button = s('#pmhome')
        self.channels_button = s('#pmchannels')
        self.back_10_sec_button = s(".icon2-10rew.small")
        self.back_button = s("#backward")
        self.forward_button = s("#forward")
        self.forward_30_sec_button = s(".icon2-30forw.small")
        self.playstop_button = s('#playstop')
        self.playstop_stop_button = s(by.xpath("//I[@class='fa fa-stop']"))
        self.playstop_play_button = s(by.xpath("//I[@class='fa fa-play']"))
        self.help_button = s('#help')

        # 5 Min Trial Player controls that should NOT be visible/enabled
        self.favorite_button = s('#favoritebutton')
        self.back_10_sec_button = s(".icon2-10rew.small")
        self.back_button = s("#backward")
        self.forward_button = s("#forward")
        self.forward_30_sec_button = s(".icon2-30forw.small")
        self.cc_menu_button = s(by.xpath("//I[@class='far buttoncaption']"))

    def initial_check_of_player_page_ongoing_event(self):
        self.home_button.should(be.enabled)
        self.channels_button.should(be.enabled)
        self.help_button.should(be.enabled)

        self.back_10_sec_button.should_not(be.visible)
        self.back_button.should_not(be.visible)
        self.forward_button.should_not(be.visible)
        self.forward_30_sec_button.should_not(be.visible)
        self.playstop_stop_button.should(be.enabled)
        self.cc_menu_button.should_not(be.visible)

        # self.volume_button.should(be.clickable)
        # self.fullscreen_button.should(be.visible).should(be.clickable)