import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'name': 'volleyball',
    'aliases': []
}

IMAGES_PATH = os.path.join(BASE_PATH, 'images')
