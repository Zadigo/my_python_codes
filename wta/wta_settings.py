import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

BASE_URLS = [
    'https://www.wtatennis.com/{}',
    'https://www.wtatennis.com/headtohead/{}/{}',
    'https://www.wtatennis.com/player/matches/{}/{}/0'
]

HTML_PATH = 'matches_parser'

CSV_FILE = 'matches'

CSV_PLAYERS = 'players'

PLAYER_URL = 'https://www.wtatennis.com/players/player/316161/title/eugenie-bouchard-0#matches'

PLAYER_HEAD_TO_HEAD_URL = 'https://www.wtatennis.com/headtohead/316161/pb:191071'

ZAPIER_URL = ''

from importlib import import_module

class Settings:
    def __init__(self):
        settings = import_module('wta_settings')
        settings_dict = settings.__dict__
        
        setattr(self, 'BASE_PATH', settings_dict['BASE_PATH'])

        if isinstance(settings_dict['HTML_PATH'], str):
            setattr(self, 'HTML', os.path.join(self.BASE_PATH, settings_dict['HTML_PATH'] + '.html'))
        else:
            raise TypeError('HTML_PATH should be a string not %s' % settings_dict['HTML_PATH'])

        setattr(self, 'CSV_FILE', os.path.join(self.BASE_PATH, settings_dict['CSV_FILE'] + '.csv'))

        setattr(self, 'CSV_PLAYERS', os.path.join(self.BASE_PATH, settings_dict['CSV_PLAYERS'] + '.csv'))

 