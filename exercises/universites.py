import re
from datetime import datetime
from collections import namedtuple

from open_data_soft import OpenDataSoft


def get_universites():
    result = OpenDataSoft('fr-esr-principaux-etablissements-enseignement-superieur@mesr')._set()
    print(result.wikipedia)

get_universites()

