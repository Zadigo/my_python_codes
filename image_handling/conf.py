import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

IMAGES_PATHS = {
    'default': os.path.join(BASE_DIR, 'images'),
    'other_folders': [],
    'new_folder': os.path.join(BASE_DIR, 'images_new'),
}

IMAGES_TYPE = (
    'jpeg','jpg',
    'png','PNG'
)

