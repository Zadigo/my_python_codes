import re
import requests
import datetime
from bs4 import BeautifulSoup
from collections import OrderedDict, namedtuple
from csv_constructor import write_csv
from ua import get_rand_agent
from urllib.parse import urlparse, urljoin, urlencode
from utils import get_age
from vsettings import IMAGES_PATH
# from vdatabase import QuerySelector


class Requestor:
    # fivb_uri = ''
    def create_request(self, uri):
        """
        Return a simple response object 
        from a request
        """
        try:
            # if self.fivb_uri:
            #     uri = self.fivb_uri
            response = requests.get(uri, get_rand_agent())
        except requests.HTTPError as e:
            raise
        else:
            return response

    @staticmethod
    def create_soup(response):
        """
        Return a soup object from BeautifulSoup
        """
        return BeautifulSoup(response.text, 'html.parser')

class PlayerProfileLinks(Requestor):
    player_page = 'http://www.%(uridomain)s.fivb.com/en/competition/teams/%(country)s/players'

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

        # We pop duplicates with
        # the set() technique
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

class PlayerProfile(PlayerProfileLinks):
    def get_player_profile(self, index=0):
        """
        Get a player's FiVB profile
        """
        main_uri = self.player_page.format(uridomain='japan2018', country='chn%20china')
        relative_uri = self.profile_links[index]
        response = super().create_request(urljoin(main_uri, relative_uri))

        # This section is to process the main section
        # of the player profile page
        soup = BeautifulSoup(response.txt, 'html.parser')
        tags = soup.find('div', class_='person')
        player_name = tags.find('h4').text
        height = tags.find(string=re.compile(r'\d+\s?cm'))
        weight = tags.find(string=re.compile(r'\d+\s?kg'))
        date_of_birth = tags.find(string=re.compile(r'\d+\/\d+\/\d{4}'))

        year_of_birth = datetime.datetime.timetuple(datetime.datetime.strptime(date_of_birth, '%d/%m/%Y'))[0]
        age = datetime.datetime.now().year - year_of_birth

        # Process the image present
        # on the main profile page
        img = soup.find('img')
        player_image_link = self.process_player_image_link(img['src'])
        
        # This section is to process the side section
        # of the player profile page
        side_section = soup.find('ul', class_='line-list')
        side_section_tags = side_section.find_all('strong')
        tags_text = [values.text for values in side_section_tags]

        position = re.match(r'(\s+|\n)([a-zA-Z]+\s?[a-zA-Z]+)', tags_text[0]).group(0).strip()
        # positions = {
        #     'setter':1,
        #     'opposite spiker':2,
        #     'middle blocker':3,
        #     'wing spiker':4,
        #     'libero':6
        # }
        spike = re.match(r'(\s+|\n+)\d{3}', str(tags_text[3])).group(0).strip()
        block = re.match(r'(\s+|\n+)\d{3}', str(tags_text[-1])).group(0).strip()

        # Player data
        player_data = [player_name, date_of_birth, age, height, weight, player_image_link]

        return urljoin(main_uri, relative_uri)

    @staticmethod
    def process_player_image_link(uri, *args):
        base = urlparse(uri)
        # We have to extract the image
        # number from the uri. We also
        # redimension the image height
        # and width within the link
        params = urlencode({
            'No':re.match(r'No\=(\d+)', base[4]).group(1),
            'type':'Press',
            'width':'1200',
            'height':'800' 
        })
        # We recompose the netloc with the
        # path to reconstruct the uri
        reconstructed_uri = base[1] + base[2] + '?' + params
        return reconstructed_uri

    @staticmethod
    def _ping(uri):
        response = super().create_request(uri)
        if response.status_code == 200:
            return 'Status code: %s' % response.status_code
        return 'The link is not valid'

# class ImageParser:
#     def __init__(self):
#         response = requests.get('https://www.fivb.org/Vis2009/Images/GetImage.asmx?No=77966&type=Press&width=300&height=450&stretch=uniformtofill', stream=True)
#         if response.status_code == 200:
#             with open(IMAGES_PATH, 'wb') as f:
#                 for chunk in response:
#                     f.write(chunk)

# ImageParser()

    

# print(PlayerProfile('http://japan2018.fivb.com/en/competition/teams/chn%20china/players').get_player_profile())
