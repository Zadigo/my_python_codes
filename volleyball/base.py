import requests
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
from ua import get_rand_agent
from urllib.parse import urlparse
from vdatabase import QuerySelector


class Requestor:
    def create_request(self, uri):
        try:
            response = requests.get(uri, get_rand_agent())
        except requests.HTTPError as e:
            raise
        else:
            return response

class PlayerProfileLinks(Requestor):
    player_page = 'http://%(domain)s.fivb.com/en/competition/teams/%(country)s/players'

    def __init__(self, uri):
        profile_links = []
        response = super().create_request(uri)

        soup =  BeautifulSoup(response.text, 'html.parser')
        # Get all the links where the href is equals to
        # the regex e.g. /en/competition/teams/chn-china/players/yixin-zheng?id=69285
        links = soup.find_all(href=re.compile(r'\/en\/competition\/teams\/\w.*\?id=\d+'))

        for link in links:
            relative_link = link['href']
            profile_links.append(relative_link)

        # We pop duplicates with the set() technique
        self.profile_links = list(set(profile_links))

    def get_ids(self):
        """
        Return the player's iDs
        """
        player_ids=[]
        links = self.profile_links
        for link in links:
            player_id = re.search(r'\?id\=(\d+)$', str(link))

            if player_id:
                player_ids.append(player_id.group(1))

        return player_ids

    # def get_names(self):
    #     """
    #     Return the player's names
    #     """
    #     player_names=[]

    # @staticmethod
    # def _parser(self, uri, *args):
    #     params = ['scheme', 'netloc', 'path', 'params', 'query', 'fragment']
    #     for arg in args
    #     parse = urlparse(uri)
    #     return parse

# re.match(r'^[a-zA-Z]+\s+\w+$')
# (player_name, player_profile_link, player_id)



# print(PlayerProfileLinks('http://japan2018.fivb.com/en/competition/teams/chn%20china/players').get_ids())
