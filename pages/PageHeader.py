from selene.api import *


class PageHeader(object):

    def __init__(self):
        self.my_tv = s('[data-target="#home"]')
        self.on_now = s('[data-target="#live-channels"]')
        self.on_demand = s('[data-target="#on-demand"]')
        self.guide = s('[data-target="#guide"]')
        self.cinema = s('[data-target="#cinema"]')
        self.recordings = s('[data-target="#recordings"]')
        self.search = s('[data-target="#search"]')
