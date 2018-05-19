import os

BASE_DIR = os.path.dirname(__file__)

DATABASE = {
    'default': {
        'name': 'bank_db.db',
        'user': '',
        'password': '',
        'path': os.path.join(BASE_DIR, 'bank_db.db')
    }
}

LOG_FILE = BASE_DIR + 'log_file.txt'