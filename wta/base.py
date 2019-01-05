import requests
import re
import datetime
import csv
import itertools
from bs4 import BeautifulSoup
from ua import get_rand_agent
from collections import namedtuple

PLAYER_URL = 'https://www.wtatennis.com/players/player/316161/title/eugenie-bouchard-0#matches'
PLAYER_HEAD_TO_HEAD_URL = 'https://www.wtatennis.com/headtohead/316161/pb:191071'
HTML_PATH = 'D:\\Programs\\Python\\repositories\\python_codes\wta\\test.html'

class Start:
    def __init__(self):
        try:
            response = requests.get(PLAYER_URL, get_rand_agent())
        except requests.HTTPError as e:
            raise
        else:
            if response.status_code == 200:
                self.response = response

            else:
                self.response = None
    @property
    def _soup(self):
        return BeautifulSoup(self.response.text, 'html.parser')

class PlayerData(Start):
    def get_data(self):
        player = namedtuple('Player', ['date_of_birth', 'age', 'height', 'playing_hand', 'country'])
        soup=self._soup

        # Get the player's age and date of birth
        player_date_of_birth = soup.find('span', class_="date-display-single")
        full_date = re.search(r'[0-9]{4}\-\d+\-\d+', str(player_date_of_birth['content'])).group(0)
        formatted_date = datetime.datetime.strptime(full_date, '%Y-%m-%d')
        age = datetime.datetime.now().year - datetime.datetime.timetuple(formatted_date).tm_year

        # Get the player's height
        player_height = soup.find('size')
        parsed_height = re.search(r'\d+\.\d+', player_height.text).group(0)
        height = int(float(parsed_height)*100)

         # Player's playing hand
        tag = soup.find('div',class_='field--name-field-playhand')
        player_playing_hand = tag.find('div',class_='even').text

        # Player's country
        tag = soup.find('div',class_='group-country')
        country = tag.find('div',class_='even').text

        return player(full_date, age, height, player_playing_hand, country)

    @staticmethod
    def convert_height(height):
        """
        Convert player's height from centimeters
        to empiric feet
        """
        return height / 30.48

class PlayerMatches:
    def get_matches(self):
        """
        Return a named tuple having the following references for a player's WTA matches:

        >>> Tournament(tour_characteristics=[], tour_details=[], player_tour_infos=[], matches=[(..., []), (...))

        `Tour characteristics` represents the characteristics of an event e.g. ['Luxembourg', 'LUX', 'Luxembourg']
        such as the town, the tournament name and the geographic area.

        `Tour details` represents the meta details of the event such as the date when it takes place,
        the tournament category and the tournament surface.

        `Player tour infos` represents the player's rank as they entered the event and their seeding
        in that specific event if it was the case.

        `Matches` is a list of tuples containing:
            - Round
            - Win/Loss
            - A list related to the characteristics of the opponent
        The list contains the opponent's seed, opponent's name, link to their profile,
        their nationality, their ranking and the score of the match.

        """
        with open(HTML_PATH, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')

            # This is the section where all
            # the informations are stored
            tags = soup.find_all('div', class_='wta-table-data')

            tournaments_played = []
            tournament = namedtuple('Tournament', ['tour_characteristics', 'tour_details', 'player_tour_infos', 'matches'])
            matches_played = []
            s=[]

            for tag in tags:
                # NOTE: This section deals with the upper
                # section of the matches tables
                # where all the information about the
                # tournament is present
                tournament_name = tag.find('span',class_='tour-name').text.strip()
                # We have to grab the tour details
                # as they are many of the 'divs'
                # with that specific class
                tour_details_tags = tag.find_all('span',class_='tour-detail')
                tour_infos_tags = tag.find('div',class_='last-row').find_all(class_='row-item')
                # Rank with which the player entered
                # that specific tournament
                player_tour_rank = re.search(r'\d+', tour_infos_tags[2].text).group(0)

                # Some players may be seeded in 
                # the tournament and we can catch that
                is_seeded = re.search(r'\d+', tour_infos_tags[3].text)
                if is_seeded:
                    player_tour_seed = is_seeded.group(0)
                else:
                    player_tour_seed = ''

                # NOTE: Here we parse the matches written in
                # the tables that we have fetched
                match_table_row = tag.find('table').find('tbody').find_all('tr')
                for data in match_table_row:
                    match_round = data.find('td', class_='round').text.strip()
                    match_result = data.find('td', class_='result').text

                    # We have to parse the opponent row
                    # specifically since there are many
                    # tags in that specific tag
                    match_opponent = data.find('td', class_='opponent')
                    if match_opponent.find(class_='opponent-seed'):
                        match_opponent_seed = match_opponent.find(class_='opponent-seed').text.strip()
                    else:
                        match_opponent_seed = ''
                    match_opponent_link = match_opponent.find('a')['href']
                    match_opponent_name = match_opponent.find('a').text.strip()
                    if re.search(r'\(([A-Z]+)\)', str(match_opponent)):
                        match_opponent_nationality = re.search(r'\(([A-Z]+)\)', str(match_opponent)).group(0)
                    else:
                        match_opponent_nationality = ''

                    match_opponent_rank = data.find('td', class_='rank').text.strip()
                    match_score = data.find('td', class_='score').text.strip()

                    match_data = match_round, match_result, \
                                [match_opponent_seed, match_opponent_name, \
                                    match_opponent_link, self.parse_nationality(match_opponent_nationality), \
                                        match_opponent_rank, match_score]
                    matches_played.append(match_data)

                tournaments_played.append(
                    tournament(
                        self.parse_tournament_name(tournament_name),
                        [detail.text.strip().lower().capitalize() for detail in tour_details_tags],
                        [player_tour_rank, player_tour_seed],
                        matches_played
                    )
                )

                # NOTE We have to reset this list
                # to prevent the new values to be
                # appended to the previous values
                # on which we iterated
                matches_played = []
            
            return tournaments_played

    @staticmethod
    def parse_tables(table):
        pass

    @staticmethod
    def parse_nationality(nationality):
        return re.search(r'[A-Z]+', nationality).group(0)

    @staticmethod
    def parse_date(unformatted_date):
        # January 7, 2018
        months = ['January', 'February', 'March', 'April', 'May',\
                    'June', 'July', 'August', 'September', 'November', 'December']

        # raw_month = re.search(r'[a-zA-Z]+', unformatted_date).group(0)
        splitted_date = unformatted_date.split(' ', 3)

        # We have to add one to get the real
        # world month
        month_index = months.index(splitted_date[0]) + 1
        d = re.search(r'\d+', splitted_date[1]).group(0)
        y = splitted_date[2]

        constructed_date = '%s-%s-%s' % (y, month_index, d)
        formatted_date = datetime.datetime.strptime(constructed_date, '%Y-%m-%d')

        return [formatted_date, formatted_date.year]

    @staticmethod
    def parse_tournament_name(tournament_name):
        """
        This function is used to return
        a list having the tournament name,
        the tournament name sigle and the
        tournament country
        """
        tournament = tournament_name.split(',', 1)
        return [
            tournament[0].strip().lower().capitalize(),
            tournament[0].strip().capitalize()[:3].upper(),
            tournament[1].strip().lower().capitalize()
        ]

    def _write_csv(self, values=[]):
        matches = self.get_matches()
