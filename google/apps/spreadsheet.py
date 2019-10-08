import time
import gspread
from collections import namedtuple
from spread_settings import JSON_KEY_FILE, SPREADSHEET
from oauth2client.service_account import ServiceAccountCredentials


class StartSpread:
    def __init__(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(JSON_KEY_FILE)
        client = gspread.authorize(credentials)
        self.spread_sheet = client.open(SPREADSHEET)


class SelectValues(StartSpread):
    pass


class UpdateValues(StartSpread):
    pass