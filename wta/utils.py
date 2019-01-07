import csv
import itertools
import datetime
import random
import math
import requests
import itertools
from urllib.parse import urljoin
from wta_settings import Settings
from base import PlayerData

def obtain_csv_urls():
    with open(Settings().CSV_FILE, 'r', newline='') as f:
        csv_file = list(csv.reader(f))
        # Remove the titles from the list
        del csv_file[0]

        # Remove duplicates
        
        for player in csv_file:
            if player[14] is not None and player[14] != '':
                yield player[14]

def obtain_heights():
    with open(Settings().CSV_PLAYERS, 'r', newline='') as f:
        csv_file = list(csv.reader(f))
        # Remove the titles from the list
        del csv_file[0]
        p=[a[3] for a in csv_file]
        yield list(itertools.dropwhile(lambda x: x == 'N/A', p))

def obtain_csv_scores():
    with open(Settings().CSV_FILE, 'r', newline='') as f:
        csv_file = list(csv.reader(f))
        # Remove the titles from the list
        del csv_file[0]
 
        for player in csv_file:
            yield player[17]

class PlayerStatistics:
    def __init__(self):
        pass

# PlayerData().get_datas(obtain_csv_urls())
print(list(obtain_csv_urls()))