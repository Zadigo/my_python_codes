from collections import namedtuple
import datetime
import csv
import statistics

class DataPoint(namedtuple('DataPoint', ['date', 'value'])):
    __slots__ = ()

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

def read_prices(csvfile, _strptime=datetime.datetime.strptime):
    with open(csvfile) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield DataPoint(date=_strptime(row['Date'], '%Y-%m-%d').date(),
                            value=float(row['Adj Close']))

prices = read_prices('D:\\Programs\\Python\\repositories\\python_codes\\exercises\\test.csv')
gains = tuple(DataPoint(day.date, 100*(day.value/prev_day.value - 1.))
                for day, prev_day in zip(prices[1:], prices))

print(gains)
