from selene.api import *


class SearchPage(object):

    def __init__(self):
        self.search_input_field = s('#search-input')
        self.cold_squad_found_event = s(by.xpath("//BUTTON[@data-vod-id='200962']"))
        self.cold_squad_first_season_select = s(by.xpath("//BUTTON[@class='season details-tab-toggle selectable'][text()='Season 1']"))
        self.cold_squad_first_season_first_episode_select = s(by.xpath("//BUTTON[@class='episode-selector selectable active'][text()='E 1']"))
        self.cold_squad_first_season_first_episode_preview_play_button = s(by.xpath("//BUTTON[@class='play play-vod'][text()='PLAY NOW']"))
