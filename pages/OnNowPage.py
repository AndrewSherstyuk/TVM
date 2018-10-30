from selene.api import *


class OnNowPage(object):

    def __init__(self):
        self.heading = s('#channels > div.heading')