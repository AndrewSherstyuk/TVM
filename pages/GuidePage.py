from selene.api import *


class GuidePage(object):

    def __init__(self):
        self.day_selector = s(".ui-selectmenu-text")
        self.sign_out_btn = s('#exit_btn')
        self.yes_on_logout_confirmation = s(".remodal-confirm")
        self.no_on_logout_confirmation = s(".remodal-cancel.focus")

    def click_on_signout_btn(self):
        self.sign_out_btn.click()

    def confirm_wish_to_logout(self):
        self.yes_on_logout_confirmation.click()

    def confirm_wish_to_not_logout(self):
        self.no_on_logout_confirmation.click()