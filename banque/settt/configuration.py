import os

APPS = [
    'banque.base1',
]

BASE_DIR = os.path.dirname(__file__)

DATABASE = {
    'default': {
        'name': 'bank.db',
        'user': '',
        'password': '',
    }
}

LOG_FILE = BASE_DIR + 'log_file.txt'

PATHS = {
    'database': os.path.join(BASE_DIR, 'bank.db')
}