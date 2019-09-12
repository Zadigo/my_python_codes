"""
This application was created to parse the tables
of matches present on the WTA website.
"""


import requests
import re
import datetime
import csv
import itertools
import time
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from ua import get_rand_agent
from collections import namedtuple
from wta_settings import Settings




# SETTINGS

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

BASE_URLS = [
    'https://www.wtatennis.com/',
    'https://www.wtatennis.com/headtohead/{}/{}',
    'https://www.wtatennis.com/player/matches/{}/{}/0'
]

PLAYER_URL = 'https://www.wtatennis.com/players/player/316161/title/eugenie-bouchard-0#matches'

PLAYER_HEAD_TO_HEAD_URL = 'https://www.wtatennis.com/headtohead/316161/pb:191071'

HTML_PATH = 'D:\\Programs\\Repositories\\my_python_codes\\wta\\src\\tennis_html\\matches.html'




def construct_player_url(path):
    return urljoin(BASE_URLS[0], path)



class Start:
    def create_request(self, uri=None, method='get', **kwargs):
        """
        Get a response from a GET request
        """
        methods = ['get', 'post']
        try:
            if method:
                if method in methods:
                    if method == 'get':
                        response = requests.get(uri, get_rand_agent())
                    
                    elif method == 'post':
                        if 'files' in kwargs:
                            files = kwargs['files']
                        else:
                            files = None

                        response = requests.post(uri, files=files, data=kwargs['data'])

                else:
                    raise KeyError('Method is not allowed (%s)' % method)

            else:
                raise KeyError('Did you specify a method? \
                                    The methods allowed are %s' % methods)

        except requests.HTTPError as e:
            print('There was an error \
                        with the HTTP request %s' % e.args)
            raise

        else:
            if response.status_code == 200:
                return response
            
            else:
                # If the response is not exploitable
                # I think its better to just raise an error
                raise requests.ConnectionError('We could not get a \
                                                response from the server.')

    def _soup(self, response):
        return BeautifulSoup(response.text, 'html.parser')

    def _soup_from_html(self, f):
        return BeautifulSoup(f, 'html.parser')

class PlayerData(Start):
    def get_data(self, uri=PLAYER_URL):
        player = namedtuple('Player', ['name', 'date_of_birth', 'age', 'height', 'height_feet', \
                                        'playing_hand', 'city', 'country', 'country_code'])
        soup = self._soup(self.create_request(uri))

        # Player name
        player_firstname = soup.find('div', class_='field--name-field-firstname').text.strip().lower().capitalize()
        player_lastname = soup.find('div', class_='field--name-field-lastname').text.strip().lower().capitalize()
        constructed_name = '%s %s' % (player_firstname, player_lastname)

        # Get the player's age and date of birth
        player_date_of_birth = soup.find('span', class_="date-display-single")
        full_date = re.search(r'[0-9]{4}\-\d+\-\d+', str(player_date_of_birth['content'])).group(0)
        formatted_date = datetime.datetime.strptime(full_date, '%Y-%m-%d')
        age = datetime.datetime.now().year - datetime.datetime.timetuple(formatted_date).tm_year

        # Get the player's height
        player_height = soup.find('size')
        
        # We have to filter against
        # NONE tags
        if player_height:
            # Some player pages do not even have
            # a height tag!!!!! Or, maybe there is
            # one but it only has a parenthesis
            if player_height.text != '(':
                # We have to protect the program against
                # data in the height tag that are not valid.
                # This includes empty spaces.
                height_data_is_valid = re.search(r'\d+\.\d+', player_height.text)
                if height_data_is_valid:
                    parsed_height = height_data_is_valid.group(0)

                else:
                    # HACK: This is quick fix
                    # to allow calculation below
                    parsed_height = 0
                height = int(float(parsed_height) * 100)

            else:
                height = 'N/A'

        else:
            height = 'N/A'

         # Player's playing hand
        tag = soup.find('div', class_='field--name-field-playhand')
        player_playing_hand = tag.find('div', class_='even').text

        # Player's country and city
        tag = soup.find('div', class_='field--name-field-birthcity').text
        if tag != 'N/A':
            city, country = tag.split(',', 1)
            _city = city.strip().lower().capitalize()
            _country = country.strip().lower().capitalize()
        else:
            _city = _country = 'N/A'

        # Player's country
        tag = soup.find('div', class_='group-country')
        country_code = tag.find('div', class_='even').text

        return player(constructed_name, formatted_date.date(), age, height, self.convert_height(height), \
                    player_playing_hand, _city, _country, country_code)

    def get_datas(self, urls, write_mode='w', sleep_time=1):
        players = []
        remapped_urls = list(map(lambda x: urljoin('https://www.wtatennis.com/', x), urls))
        
        print(len(remapped_urls), 'links to parse')
        print('Getting details from:')
        for url in remapped_urls:
            print(url)
            player = self.get_data(uri = url)
            players.append(player)
            
            time.sleep(sleep_time)
        
        with open(Settings().CSV_PLAYERS, write_mode, newline='') as f:
            csv_file = csv.writer(f)
            csv_file.writerow(['full_name', 'date_of_birth', 'age', 'height_metrique', 'height_imperial'\
                                'playing_hand', 'city_of_birth', 'state_of_birth', 'country_code'])
            for player in players:
                csv_file.writerow(player)
        
        print('Success!')

    @staticmethod
    def convert_height(height):
        """Convert player's height from centimeters
        to empiric feet
        """
        # The incoming height to convert
        # might be non valid or n/a
        if height == 'N/A' or not isinstance(height, (int, float)):
            return 'N/A'
        return round(height / 30.48, 1)


class PlayerMatchesHtml(Start):
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
            # soup = BeautifulSoup(f, 'html.parser')
            soup = self._soup_from_html(f)

            # This is the section where all
            # the informations stored are
            # parsed as a whole
            tags = soup.find_all('div', class_='wta-table-data')

            tournaments_played = []
            tournament = namedtuple('Tournament', ['tour_characteristics', \
                                        'tour_details', 'player_tour_infos', 'matches'])
            matches_played = []
            s = []

            for tag in tags:
                # This section deals with the upper
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
                    player_tour_seed = self.parse_seeding(is_seeded.group(0))
                else:
                    player_tour_seed = None

                print('Fetching: %s' % tournament_name)

                # Here we parse the matches present in
                # the table that we have fetched above
                match_table_row = tag.find('table').find('tbody').find_all('tr')
                for data in match_table_row:
                    match_round = data.find('td', class_='round').text.strip()
                    match_result = data.find('td', class_='result').text

                    # We have to parse the opponent row
                    # specifically since there are many
                    # tags in that specific section
                    match_opponent = data.find('td', class_='opponent')
                    # Some players might not have a
                    # seeding! We have to take care
                    # of that here
                    has_seeding = match_opponent.find(class_='opponent-seed')
                    if has_seeding:
                        match_opponent_seed = has_seeding.text.strip()
                    else:
                        match_opponent_seed = None

                    # This part breaks because of the BYE
                    # that sometimes occurs in the start
                    # of certain tournaments.
                    # IMPORTANT: This still generates a csv row so it
                    # would be interesting to find an alternative
                    has_opponent_link = match_opponent.find('a')
                    if has_opponent_link:
                        match_opponent_link = has_opponent_link['href']
                    else:
                        match_opponent_link = None

                    has_opponent_name = match_opponent.find('a')
                    if has_opponent_name:
                        match_opponent_name = has_opponent_name.text.strip()

                        has_opponent_nationality = re.search(r'\(([A-Z]+)\)', str(match_opponent))
                        if has_opponent_nationality:
                            match_opponent_nationality = has_opponent_nationality.group(0)

                        else:
                            match_opponent_nationality = None

                    else:
                        match_opponent_name = None

                    match_opponent_rank = data.find('td', class_='rank').text.strip()
                    match_score = data.find('td', class_='score').text.strip()

                    # Here we determine the amounts of sets played
                    # so as if the first set was won or not
                    sets_statistics = self.parse_score(match_score, match_result)

                    # This creates a match data tuple
                    match_data = match_round, match_result, \
                                [match_opponent_seed, match_opponent_name, \
                                    match_opponent_link, self.parse_nationality(match_opponent_nationality), \
                                        match_opponent_rank, match_score] + sets_statistics
                    matches_played.append(match_data)

                tournaments_played.append(
                    tournament(
                        self.parse_tournament_name(tournament_name),
                        [detail.text.strip().lower().capitalize() for detail in tour_details_tags],
                        [player_tour_rank, player_tour_seed],
                        matches_played
                    )
                )

                # NOTE: We have to reset this list
                # to prevent the new values to be
                # appended to the previous values
                # on which we iterated
                matches_played = []
            
            return tournaments_played

    @staticmethod
    def parse_nationality(nationality):
        return re.search(r'[A-Z]+', nationality).group(0)

    @staticmethod
    def parse_date(unformatted_date):
        # January 7, 2018
        months = ['January', 'February', 'March', 'April', 'May',\
                    'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        splitted_date = unformatted_date.split(' ', 3)

        # We have to add one to get the real
        # world month
        month_index = months.index(splitted_date[0]) + 1
        d = re.search(r'\d+', splitted_date[1]).group(0)
        y = splitted_date[2]

        constructed_date = '%s-%s-%s' % (y, month_index, d)
        formatted_date = datetime.datetime.strptime(constructed_date, '%Y-%m-%d').date()

        return [formatted_date, formatted_date.year]

    @staticmethod
    def parse_tournament_name(tournament_name):
        """
        This function is used to return
        a list having the tournament name,
        the tournament name sigle and the
        tournament country
        """
        tournament = tournament_name.split(',', 2)
        
        return [
            tournament[0].strip().lower().capitalize(),
            tournament[0].strip().capitalize()[:3].upper(),
            tournament[1].strip().lower().capitalize()
        ]

    @staticmethod
    def parse_seeding(seed):
        has_value = re.search(r'(\d+|\w+)', seed)
        if has_value:
            return has_value.group(0)
        return None

    @staticmethod
    def parse_score(score, match_result):
        first_set=''
        splitted_score = score.split(' ')
        if '' in splitted_score:
            splitted_score = [score for score in splitted_score if score != '']

        if match_result == 'W':
            has_lost_first_set = re.match(r'([0-4]\-6|[5-6]\-7)', splitted_score[0])
            if has_lost_first_set:
                first_set = 'Loss'

            else:
                first_set = 'Win'

        elif match_result == 'L':
            has_won_first_set = re.match(r'^(6\-[0-4]|7\-[5-6])', splitted_score[0])
            if has_won_first_set:
                first_set = 'Loss'

            else:
                first_set = 'Win'

        number_of_sets=''

        if len(splitted_score) == 3:
            number_of_sets = 'Three'

        elif len(splitted_score) == 2:
            number_of_sets = 'Two'

        elif 'RET' in splitted_score:
            number_of_sets = 'RET'

        else:
            number_of_sets = None
        
        return [number_of_sets, first_set]
        
    def _write_csv(self, mode='w'):
        # "['Tashkent', 'TAS', 'Uzbekistan']","['September 24, 2018', 'International', 'Hard']","['107', '']","[('Round 32', 'L', ['', 'Nao Hibino', '/players/player/320238/title/Nao-HIBINO', 'JPN', '128', '6-3 6-3'])]"
        matches = list(reversed(self.get_matches()))

        with open(Settings().CSV_FILE, mode=mode, newline='') as f:
            csv_file = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_file.writerow(['tour', 'tour_code', 'tour_country', 'date', 'year', 'month', \
                                'tour_type', 'tour_surface', 'player_rank', 'player_seed', \
                                'match_round', 'match_result', 'opp_seed', 'opp_name', 'opp_profile_link',
                                'opp_nationality', 'opp_rank', 'match_score', 'num_sets', 'first_set_result'])

            for a in matches:
                tour_characteristics = a[0]
                tour_details = a[1]
                player_tour_infos = a[2]
                matches = a[3]

                # Convert/format the date
                parsed_date = self.parse_date(tour_details[0])
                tour_details[0] = str(parsed_date[0])
                tour_details.insert(1, parsed_date[0].year)
                tour_details.insert(2, parsed_date[0].month)

                number_of_matches = len(matches)
                
                for match in matches:
                    to_append_first = [match[0], match[1]]
                    to_append_second = match[2]
                    constructed_row = tour_characteristics + tour_details + player_tour_infos + to_append_first + to_append_second
                    csv_file.writerow(constructed_row)

        print('Success!')

import json

class StatisticCreator(Start):
    # def __init__(self):
    #     path = os.path.join(BASE_PATH, 'match_stats.html')
    #     path_to_write = os.path.join(BASE_PATH, 'match_stats.txt')
    #     with open(path, 'r', encoding='utf-8') as f:
    #         soup = super()._soup_from_html(f)

    #         links = soup.find_all(href=re.compile(r'https\:\/\/matchstat.com\/tennis\/match\-stats\/w\/\d+$'))
    #         with open(path_to_write, 'w', encoding='utf-8') as f_to_write:
    #             for link in links:
    #                 f_to_write.writelines(link['href'])
    #                 f_to_write.writelines('\n')

    def get_statistics(self):
        path = os.path.join(BASE_PATH, 'test.json')
        response = super().create_request('https://matchstat.com/tennis/match-stats/w/8561159')
        statistics = response.json()['stats']

        # We have to clean the data
        statistics[0].pop('match_stats_id')
        statistics[0].pop('team')
        statistics[0].pop('serve_speed_fastest')
        statistics[0].pop('serve_speed_1st_avg')
        statistics[0].pop('serve_speed_2nd_avg')
        statistics[0].pop('net_approaches')
        statistics[0].pop('odds')
        statistics[0].pop('match')

        statistics[1].pop('match_stats_id')
        statistics[1].pop('team')
        statistics[1].pop('serve_speed_fastest')
        statistics[1].pop('serve_speed_1st_avg')
        statistics[1].pop('serve_speed_2nd_avg')
        statistics[1].pop('net_approaches')
        statistics[1].pop('odds')
        statistics[1].pop('match')

        # Rows
        statisctic_row = [statistics[0]['serve_1st_attempts'],
                            statistics[0]['player_fullname'],
                            statistics[0]['total_points'],
                            statistics[0]['points_won'],
                            statistics[0]['serve_games_total'],
                            statistics[0]['serve_games_won'],
                            statistics[0]['aces'],
                            statistics[0]['double_faults'],
                            statistics[0]['serve_1st_total'],
                            statistics[0]['serve_1st_won'],
                            statistics[0]['serve_2nd_total'],
                            statistics[0]['serve_2nd_won'],
                            statistics[0]['return_points_total'],
                            statistics[0]['return_points_won'],
                            statistics[0]['return_break_points_total'],
                            statistics[0]['return_break_points_won'],
                            statistics[0]['winners'],
                            statistics[0]['unforced_errors']]
        
        print(statisctic_row)
            
# StatisticCreator().get_statistics()


# REGEX score
# ^(6|7)\-?(\d)\s?(\1)\-?(\2)$
# ^(6|7)\-?([0-4])\s?(6|7)\-?([0-4])$
# 6-0 6-0 ^(6\-0)\s?(\1)$