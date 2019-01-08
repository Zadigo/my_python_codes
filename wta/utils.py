import csv
import itertools
import datetime
import random
import math
import requests
import collections
from urllib.parse import urljoin
from wta_settings import Settings
from base import PlayerData

def csv_handle():
    csv_file = open(Settings().CSV_PLAYERS, 'r+', newline='')
    return [csv.reader(csv_file), csv.writer(csv_file), csv_file]

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


class Lenght:
    _metric = {
        'ft': 0.3048,
        'm': 0.01
    }

    def __init__(self, value, metric):
        self.value = value
        self.metric = metric

    def __add__(self, value):
        result = self.value + value
        return Lenght(result, self.metric)

    def __sub__(self, value):
        result = self.value - value
        return Lenght(result, self.metric)

    def __repr__(self):
        return "Lenght(%s, %s)" % (self.value, self.metric)

    def convert_to_feet(self):
        return round(self.value / (self._metric['ft'] * 100), 1)

    def _convert_to_feet(self):
        result = str(round(self.value / (self._metric['ft'] * 100), 1)).split('.', 1)
        return "%s'%s\"" % (result[0], result[1])


class HeightCalculator:
    def __init__(self, values=[]):
        if not isinstance(values, (list, tuple)):
            raise
        self.values = values
    
    def __iter__(self):
        result = 0
        for value in self.values:
            result += value
        yield round(result / len(self.values), 1)

    def __str__(self):
        return 'HeightCalculator(%s)' % self.__iter__()


class PlayerLinkCreator:
    def __init__(self, url, iterable):
        if not isinstance(iterable, (tuple, list)):
            raise TypeError('"%s" should be a list or a tuple' % iterable)

        if len(iterable) == 0:
            raise IndexError('There is nothing to iterate '
                                'from "%s"' % iterable)

        self.paths = iterable
        self.url = url

    def __iter__(self):
        for path in self.paths:
            for item in path:
                yield urljoin(self.url, item)

    def __str__(self):
        return 'PlayerLinkCreator(%s)' % self.__iter__()

# class A(PlayerLinkCreator):
#     def __init__(self, iterable):
#         return super().__init__('http://www.google.com/c/', iterable)

def get_duplicates():
    handle = csv_handle()
    csv_list = list(handle[0])
    s=collections.deque()
    h=[]
    for i in range(0,len(csv_list)):
        h.append(csv_list[i][0])
        if i == 0:
            pass
        if i == 1:
            s.append(csv_list[i])
        if i > 1:
            player = csv_list[i][0]
            if player not in h:
                s.append(csv_list[i])
        else:
            pass
    handle[2].close()

get_duplicates()
