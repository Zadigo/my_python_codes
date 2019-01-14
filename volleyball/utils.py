import datetime
import json
import os
from vsvettings import BASE_PATH


def get_age(date_of_birth):
    year_of_birth = datetime.datetime.timetuple(
        datetime.datetime.strptime(date_of_birth, '%d/%m/%Y'))[0]
    return datetime.datetime.now().year - year_of_birth


def countries():
    def _wrap(file_name='country_list.json'):
        with open('D:\\Programs\\Repositories\\my_python_codes\\volleyball\\country_list.json', 'r', encoding='utf-8') as f:
            yield json.load(f)
    return _wrap

import sys
print(sys.path)
