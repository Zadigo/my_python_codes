import re
import requests
import datetime
from bs4 import BeautifulSoup
from collections import OrderedDict, namedtuple
from csv_constructor import write_csv
from ua import get_rand_agent
from urllib.parse import urlparse, urljoin, urlencode
from utils import get_age
from vsettings import IMAGES_PATH, PLAYER_PAGE_URI
# from vdatabase import QuerySelector


class Requestor:
    def create_request(self, uri):
        """
        Return a simple response object 
        from a request
        """
        try:
            response = requests.get(uri, get_rand_agent())
        except requests.HTTPError as e:
            raise
        else:
            return response

    def _ping(self, uri):
        """
        This method can be used to test the
        validity of a link
        """
        response = self.create_request(uri)
        if response.status_code == 200:
            return 'Status code: %s' % response.status_code
        return 'The link is not valid'

    @staticmethod
    def create_soup(response):
        """
        Return a soup object from BeautifulSoup
        """
        return BeautifulSoup(response.text, 'html.parser')

class TeamProfileLinks(Requestor):
    def __init__(self):
        profile_links = []
        response = super().create_request(PLAYER_PAGE_URI)

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

    @staticmethod
    def _output(values=[]):
        with open('', 'w', encoding='utf-8') as f:
            for value in values:
                f.writelines(value)
                f.writelines('\n')

class PlayerProfile(TeamProfileLinks):
    def get_player_profile(self, index=0, with_image=False):
        """
        Get a player's FiVB profile

        To get a specific player use index
        """
        # We get a specific index within the player's
        # profile links that was generated
        relative_uri = self.profile_links[index]

        # We send a request using the base uri (team page)
        # and the uri the player profile page that we got
        # from that specific page
        response = super().create_request(urljoin(PLAYER_PAGE_URI, relative_uri))

        # This section is to process the main section
        # of the player profile page e.g. middle section
        soup = super().create_soup(response)
        tags = soup.find('div', class_='person')
        player_name = str(tags.find('h4').text).strip()
        height = tags.find(string=re.compile(r'\d+\s?cm'))
        weight = tags.find(string=re.compile(r'\d+\s?kg'))
        date_of_birth = tags.find(string=re.compile(r'\d+\/\d+\/\d{4}'))

        # Here we calculate the player's age
        year_of_birth = datetime.datetime.timetuple(datetime.datetime.strptime(date_of_birth, '%d/%m/%Y'))[0]
        age = datetime.datetime.now().year - year_of_birth

        # Process the image present
        # on the player's profile page
        img = soup.find('img', alt=player_name)
        player_image_link = self.process_player_image_link(img['src'])
        
        # This section is to process the side section
        # of the player's profile page
        side_section = soup.find('ul', class_='line-list')
        side_section_tags = side_section.find_all('strong')
        tags_text = [values.text for values in side_section_tags]

        position = re.match(r'(\s+|\n)([a-zA-Z]+\s?[a-zA-Z]+)', tags_text[0]).group(0).strip()
        positions_index = {
            'setter':1,
            'opposite spiker':2,
            'middle blocker':3,
            'wing spiker':4,
            'libero':6
        }
        spike = re.match(r'(\s+|\n+)\d{3}', str(tags_text[3])).group(0).strip()
        block = re.match(r'(\s+|\n+)\d{3}', str(tags_text[-1])).group(0).strip()

        # Player data
        if with_image:
            player_data = [
                player_name,
                date_of_birth,
                age,
                height,
                weight,
                position,
                spike,
                block,
                player_image_link
            ]
        else:
            player_data = [
                player_name,
                date_of_birth,
                age,
                height,
                weight,
                position,
                spike,
                block
            ]

        print(player_data)

    @staticmethod
    def process_player_image_link(image_uri, width=1200, height=800):
        """
        This definition creates a new link
        with a custom image size

        """
        base = urlparse(image_uri)
        # We have to extract the image
        # number from the uri. We also
        # redimension the image height
        # and width within the link
        params = urlencode({
            'No':re.match(r'No\=(\d+)', base[4]).group(1),
            'type':'Press',
            'width':width,
            'height':height 
        })
        # We recompose the netloc with the
        # path to reconstruct the uri
        reconstructed_uri = base[1] + base[2] + '?' + params
        return reconstructed_uri

TeamProfileLinks()