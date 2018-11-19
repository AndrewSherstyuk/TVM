from selene.api import *


class PlayerPage(object):

    def __init__(self):

        # Player Controls below the progress bar
        self.home_button = s('#pmhome')
        self.channels_button = s('#pmchannels')
        self.favorite_button = s('#favorite')
        self.playstop_button = s('#playstop')
        self.cc_menu_button = s('#captionsmenu')
        self.help_button = s('#help')
        self.volume_button = s('#mute')
        self.fullscreen_button = s('#fullscreenbutton')

        self.channels_line = s('#channels-player')
        self.channels_left_arrow_button = s('#channels-leftarrow')
        self.channels_right_arrow_button = s('#channels-rightarrowblock')

        # Player Controls above the progress bar
        self.left_infobox = s('#left-infobox')
        self.left_arrow_button = s('#leftarrowblock')
        self.right_arrow_button = s('#rightarrowblock')

        self.player_window = s('#player')

    def click_on_the_player_to_unhide_controls(self):
        self.player_window.double_click()
        self.player_window.hover()

    def tap_on_the_first_channel_in_the_list(self):
        self.first_channel_in_the_list.click()

    # Actions on Player Controls
    def tap_on_home_button(self):
        self.home_button.click()
        return

    def tap_on_channels_button(self):
        self.channels_button.double_click()
        self.player_window.hover()
        return

    def tap_on_favorite_button(self):
        self.favorite_button.click()
        return

    def tap_on_playstop_button(self):
        self.playstop_button.click()
        return

    def tap_on_cc_button(self):
        self.cc_menu_button.click()
        return

    def tap_on_help_button(self):
        self.help_button.click()
        return

    def tap_on_volume_button(self):
        self.volume_button.click()

    def tap_on_fullscreen_button(self):
        self.fullscreen_button.click()


