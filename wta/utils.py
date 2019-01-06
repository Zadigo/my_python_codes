import csv
import itertools
import random
import math
import requests
import itertools
from wta_settings import Settings

def obtain_csv_urls():
    with open(Settings().CSV_FILE, 'r', newline='') as f:
        csv_file = list(csv.reader(f))
        # Remove the titles from the list
        del csv_file[0]

        for player in csv_file:
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

print(list(obtain_heights()))

class PlayerStatistics:
    def __init__(self):
        pass
