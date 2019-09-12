import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPS = [
    'bank.database.manager',
]

DATABASE = {
    'default': {
        'ENGINE': 'sqlite',
        'NAME': 'test',
        # 'USER': 'test',
        # 'PASSWORD': 'test',
    }
}

LOG_FILE = os.path.join(BASE_DIR, 'log_file.txt')
