import re
import requests
import datetime
import time
import csv
from bs4 import BeautifulSoup
from collections import namedtuple, deque
from ua import get_rand_agent
from urllib.parse import urlparse, urljoin, urlencode
from utils import get_age
from vsettings import IMAGES_PATH, PLAYER_PAGE_URI


PLAYER_CSV='D:\\Programs\\Repositories\\my_python_codes\\volleyball\\test.csv'

PLAYER_PAGE_URI = 'http://%s.fivb.com/en/competition/teams/%s/players' 

COUNTRIES = ['arg-argentina', 'aze-azerbaijan', 'bra-brazil',
            'bul-bulgaria', 'cmr-cameroon', 'can-canada',
            'chn-china', 'cub-cuba', 'dom-dominican%20republic',
            'ger-germany', 'ita-italy', 'jpn-japan', 'kaz-kazakhstan',
            'ken-kenya', 'kor-korea', 'mex-mexico',
            'ned-netherlands', 'pur-puerto%20rico', 'rus-russia',
            'srb-serbia', 'tha-thailand', 'tto-trinidad%20%20tobago',
            'tur-turkey', 'usa-usa']


class Mixins:
    main_url = 'http://%s.fivb.com/'
    database = {
        'name': 'volleyball',
        'aliases': []
    }
    
    def __setattr__(self, name, value):
        if name == 'database':
            if not isinstance(value, dict):
                raise

            else:
                if 'name' not in value:
                    raise
                if 'aliases' not in value:
                    value.update({'aliases': []})

        if name == 'main_url':
            check = re.match(r'http\:\/\/(www)?\.\w+\.\w+', value)
            if not check:
                raise

        return super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == 'database':
            database = self.database.get('name')
            aliases = self.database.get('aliases')
            return aliases.append('database')

        return self['database']


class PlayerPages(dict):
    def __init__(self, domain):
        # Converts a the COUNTRIES list to a
        # usable dict that can be used for
        # various tasks
        for country in COUNTRIES:
            search = re.match(r'(\w{3}\-(\w.*))',country)
            
            if not search:
                print('%s is badly constructed. \
                        Did you mean %s-%s' % (country, country[:3], country))

            else:
                uri = f'http://{domain}.fivb.com/en/competition/teams/{country}/players'
                data = [search.group(0), uri]

                self.update({search.group(2): data})

    def __repr__(self):
        return 'PlayerPages(%s)' % self.__class__

    def get_link(self, country):
        return self.get(country)[1]


class Player(namedtuple('Player', ['player_name', 'height', 'weight', 
                        'date_of_birth', 'age', 'position', 'spike', 'block', 'country'])):
    __slots__ = ()


class ProfileLinks(list, Mixins):
    @property
    def remove_duplicate(self):
        # We pop duplicates with the set() technique
        return list(set(self.__iter__()))

    def _append(self, path, domain=None):
        full_url = urljoin(self.main_url % domain, path)
        self.append(full_url)
        return self.__str__()

    def __str__(self):
        return super().__str__()


class Requestor:
    def create_request(self, uri):
        try:
            response = requests.get(uri, get_rand_agent())
        except requests.HTTPError as e:
            raise
        else:
            return response

    @classmethod
    def _ping(cls, uri):
        response = cls.create_request(uri)
        if response.status_code == 200:
            return 'Status code: %s' % response.status_code
        return 'The link is not valid'

    @staticmethod
    def create_soup(response):
        return BeautifulSoup(response.text, 'html.parser')


class TeamProfile(Requestor):
    def __init__(self, domain=None, country='russia'):
        if not domain:
            print('WARNING: No domain was specified')

        print('Getting  links on %s\'s team volleyball page' % country.capitalize())
        print('-' * 60)

        pages = PlayerPages(domain)
        response = super().create_request(pages.get_link(country))
        soup =  self.create_soup(response)

        # Get all the links where the href is equals to
        # the regex e.g. /en/competition/teams/chn-china/players/yixin-zheng?id=69285
        # By doing so we can send a request to get each
        # player's profile
        links = soup.find_all(href=re.compile(r'\/en\/competition\/teams\/\w.*\?id=\d+'))

        profile_links = ProfileLinks()
        for link in links:
            relative_link = link['href']
            profile_links._append(relative_link, domain=domain)
        
        # We pop duplicates with the set() technique
        self.profile_links = profile_links.remove_duplicate


class PlayerProfile(TeamProfile):
    def get_player(self, player_index=0):
        """
        Get a player's FiVB profile
        """
        # We get a specific index within the player's
        # profile links that was generated
        relative_uri = self.profile_links[player_index]

        # We send a request using the base uri (team page)
        # and the uri the player profile page that we got
        # from that specific page
        response = super().create_request(urljoin(PLAYER_PAGE_URI, relative_uri))

        # This section is to process the main section
        # of the player profile page e.g. middle section
        soup = super().create_soup(response)
        
        return self.process_html(soup)

    def get_players(self):
        responses=[]
        soups=[]
        player_datas=[]
        uris = self.profile_links

        for uri in uris:
            print('Fetching: %s' % uri)
            responses.append(super().create_request(uri))
            time.sleep(1)

        for response in responses:
            soups.append(super().create_soup(response))

        for soup in soups:
            player_data = self.process_html(soup)
            player_datas.append(player_data)

        return player_datas

    def process_html(self, soup):
        # Main player profile section
        tags = soup.find('div', class_='person')

        player_name = str(tags.find('h4').text).strip()
        height = tags.find(string=re.compile(r'\d+\s?cm'))
        weight = tags.find(string=re.compile(r'\d+\s?kg'))
        date_of_birth = tags.find(string=re.compile(r'\d+\/\d+\/\d{4}'))

        # Here we calculate the player's age
        # year_of_birth = datetime.datetime.timetuple(datetime.datetime.strptime(date_of_birth, '%d/%m/%Y'))[0]
        # age = datetime.datetime.now().year - year_of_birth
        age = get_age(date_of_birth)

        # Process the image present on the player's
        # profile page
        img = soup.find('img', alt=player_name)
        player_image_link = self.process_player_image(img['src'])

        # This section is to process the side section
        # of the player's profile page
        side_section = soup.find('ul', class_='line-list')
        side_section_tags = side_section.find_all('strong')
        tags_text = [values.text for values in side_section_tags]

        position = re.match(r'(\s+|\n)([a-zA-Z]+\s?[a-zA-Z]+)', tags_text[0]).group(0).strip()

        spike = re.match(r'(\s+|\n+)\d{3}', str(tags_text[3]))
        block = re.match(r'(\s+|\n+)\d{3}', str(tags_text[-1]))
        if spike:
            spike_data = spike.group(0).strip()
        else:
            spike_data = 0
        if block:
            block_data = block.group(0).strip()
        else:
            spike_data = 0

        # We have to reprocess the height 
        # and weight to take out the metric
        height = re.match(r'\d+', height).group(0)
        weight = re.match(r'\d+', weight).group(0)

        # Player(player_name, date_of_birth, age, height, weight,
        #        position, positions_index[position], spike, block)
        player_data = [player_name, date_of_birth, age, height, weight,
                        position, spike_data, block_data, player_image_link]

        return player_data

    def _write_players(self, filename='volleyball', titles=[], mode='w'):
        players = self.get_players()
        titles =  ['player_name', 'date_of_birth', 'age', 'height', 'weight',
                    'position', 'spike', 'block', 'player_image_link']

        with open(PLAYER_CSV, mode, newline='') as csvfile:
            print('Writing players...')

            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)                
            csv_writer.writerow(titles)

            for player in players:
                csv_writer.writerow(player)
        
        print('Success!')

    @staticmethod
    def process_player_image(image_uri, width=1200, height=800):
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

start = PlayerProfile(domain='japan2018', country='brazil')
start._write_players(mode='a')