from selene.api import *


class PlayerPage(object):

    def __init__(self):

        # Player Controls below the progress bar
        self.home_button = s('#pmhome')
        self.channels_button = s('#pmchannels')
        self.favorite_button = s('#favoritebutton')
        self.favorite_button_not_clicked = ["xpath", '//favorite.playermenuitem.focus[contains(@css, "fa.fa-heart-o")]']
        self.back_10_sec_button = s(".icon2-10rew.small")
        self.back_button = s(".fa.fa-backward")
        self.forward_button = s(".fa.fa-forward")
        self.forward_30_sec_button = s(".icon2-30forw.small")
        self.playstop_button = s('#playstop')
        self.playstop_stop_button = s(by.xpath("//I[@class='fa fa-stop']"))
        self.playstop_play_button = s(by.xpath("//I[@class='fa fa-play']"))

        self.cc_menu_button = s(by.xpath("//I[@class='far buttoncaption']"))
        self.cc_menu_english_option = s(by.xpath("//BUTTON[@class='caption selectable'][text()='English']"))
        self.cc_menu_off_option = s(by.xpath("//BUTTON[@id='captionoff']"))

        self.help_button = s('#help')

        # The Help panel gets visible when the Help button is tapped/clicked. It contains 4 items
        self.help_panel = s('#help-panel')
        self.somethingwrong_option = s(by.xpath("//SPAN[@data-translate='pl_main_modal_panel_form']"))
        self.showplaybackstats_option = s(by.xpath("//SPAN[@data-translate='pl_main_modal_panel_show_stats'][text()='Show playback stats']"))
        self.reloadstream_option = s(by.xpath("//SPAN[@data-translate='pl_main_modal_panel_reload'][text()='Reload stream']"))
        self.close_option = s(by.xpath("//SPAN[@data-translate='pl_main_modal_panel_close'][text()='Close']"))

        # The Help form appears when Something Wrong option is selected from the Help panel
        self.help_form = s("#help-form")
        self.help_form_input_field = s('#message')
        self.help_form_close_button = s(by.xpath("(//BUTTON[@data-remodal-action='cancel'][text()='Close'][text()='Close'])[2]"))
        self.help_form_submitreport_button = s(by.xpath("//BUTTON[@data-remodal-action='confirm'][text()='Submit report']"))
        self.help_form_report_received_notification = s("#debug-data-modal")
        self.help_form_report_received_notification_heading = s(by.xpath("//H1[@class='heading-done'][text()='Your report has been received']"))
        self.help_form_report_received_notification_confirm_button = s(by.xpath("//BUTTON[@data-remodal-action='confirm'][text()='Continue']"))

        # The Playback Stats popup appears when the Playback Stats option is selected from the Help menu
        self.playbackstats_popup = s("#playback-stats")
        self.playbackstats_popup_close_button = s(by.xpath("//DIV[@class='close'][text()='[x]']"))

        self.help_form_empty_report_notification = s("#tvm-alert")
        self.help_form_empty_report_notification_title = s(by.xpath("//H1[@class='title'][text()='Oops!']"))
        self.help_form_empty_report_notification_message = s(by.xpath("//H3[@class='message'][text()='You have to fill the form before sending report']"))
        self.help_form_empty_report_notification_conrim_button = s(by.xpath("(//BUTTON[@data-remodal-action='confirm'][text()='OK'][text()='OK'])[1]"))

        self.volume_button = s('#mutebutton')
        self.volume_button_off_state = s(by.css('fa fa-volume-off'))
        self.volume_button_on_state = s(by.css('fa fa-volume-up'))

        self.fullscreen_button = s('#fullscreenbutton')

        self.channels_line = s('#channels-player')
        self.channels_left_arrow_button = s('#channels-leftarrow')
        self.channels_right_arrow_button = s('#channels-rightarrowblock')

        # Player Controls above the progress bar
        self.left_infobox = s('#left-infobox')
        self.left_arrow_button = s('#leftarrowblock')
        self.right_arrow_button = s('#rightarrowblock')

        self.player_window = s('#player')

    def initial_check_of_player_page(self):
        self.home_button.should(be.clickable)
        self.channels_button.should(be.clickable)
        self.favorite_button.should(be.clickable)
        self.playstop_stop_button.should(be.visible)
        self.cc_menu_button.should(be.clickable)
        self.help_button.should(be.clickable)
        self.volume_button.should(be.clickable)
        self.fullscreen_button.should(be.clickable)

    def initial_check_of_player_page_ongoing_event(self):
        self.home_button.should(be.clickable)
        self.channels_button.should(be.visible).should(be.clickable)
        self.favorite_button.should(be.visible).should(be.clickable)
        self.back_10_sec_button.should_not(be.visible)
        self.back_button.should_not(be.visible)
        self.forward_button.should_not(be.visible)
        self.forward_30_sec_button.should_not(be.visible)
        self.playstop_stop_button.should(be.visible).should(be.visible)
        self.cc_menu_button.should(be.visible).should(be.clickable)
        self.help_button.should(be.visible).should(be.clickable)
        self.volume_button.should(be.visible).should(be.clickable)
        self.fullscreen_button.should(be.visible).should(be.clickable)

    def initial_check_of_player_page_recorded_event(self):
        self.home_button.should(be.visible).should(be.clickable)
        self.channels_button.should_not(be.visible).should_not(be.visible)
        self.favorite_button.should_not(be.visible)
        self.back_10_sec_button.should(be.visible)
        self.back_button.should(be.visible).should(be.visible)
        self.forward_button.should(be.visible).should(be.visible)
        self.forward_30_sec_button.should(be.visible).should(be.visible)
        self.playstop_stop_button.should(be.visible).should(be.visible)
        self.cc_menu_button.should(be.visible).should(be.clickable)
        self.help_button.should(be.visible).should(be.clickable)
        self.volume_button.should(be.visible).should(be.clickable)
        self.fullscreen_button.should(be.visible).should(be.clickable)

    def make_player_controls_visible(self):
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


