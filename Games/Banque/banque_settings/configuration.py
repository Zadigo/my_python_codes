import os

APPS = [
    'banque.base1',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'default': {
        'ENGINE': 'Banque.banque_database.manager',
        'NAME': 'db.sqlite',
        'USER': '',
        'PASSWORD': '',
    }
}

LOG_FILE = os.path.join(BASE_DIR, 'log_file.txt')

# MIDDLEWARE = [
#     'Banque.'
# ]

# PATHS = {
#     'database': os.path.join(BASE_DIR, 'bank.db')
# }

print(LOG_FILE)