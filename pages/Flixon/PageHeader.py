from selene.api import *


class PageHeader(object):

    def __init__(self):

        # Top Nav tabs
        self.my_tv = s('[data-target="#home"]')
        self.on_now = s('[data-target="#live-channels"]')
        self.on_demand = s('[data-target="#on-demand"]')
        self.guide = s('[data-target="#guide"]')
        self.cinema = s('[data-target="#cinema"]')
        self.recordings = s('[data-target="#recordings"]')
        self.search = s('[data-target="#search"]')

        #Log Out and Notification buttons
        self.sign_out_btn = s('#exit_btn')
        self.yes_on_logout_confirmation = s(".remodal-confirm")
        self.no_on_logout_confirmation = s(".remodal-cancel.focus")

    def click_on_signout_btn(self):
        self.sign_out_btn.click()

    def confirm_wish_to_logout(self):
        self.yes_on_logout_confirmation.click()

    def log_out(self):
        self.sign_out_btn.should(be.clickable)
        self.click_on_signout_btn()
        self.confirm_wish_to_logout()

    def confirm_wish_to_not_logout(self):
        self.no_on_logout_confirmation.click()
