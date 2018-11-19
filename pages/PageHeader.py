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