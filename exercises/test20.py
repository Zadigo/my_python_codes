from collections import namedtuple
import datetime
import csv
import statistics

CSV_file = 'D:\\Programs\\Python\\repositories\\python_codes\\exercises\\test1.csv'

class Player(namedtuple('Player', ['name', 'height', 'finish'])):
    __slots__ = ()

    def __lt__(self, other):
        return self.time < other.time

def read_csv(csv_object=CSV_file):
    player = namedtuple('Player', ['name', 'height', 'finish'])
    with open(csv_object, 'r', encoding='utf-8') as f:
        csv_dict = csv.DictReader(f)
        for value in csv_dict:
            yield Player(value['name'],value['height'],
                            datetime.datetime.strptime(value['finish'], '%H:%M:%S'))

players = list(read_csv())
