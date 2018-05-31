import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CONSTRUCTED_DIRS = [
    {
        'downloads': os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'Downloads'),
    }
]

CLOUD_DIRECTORY = ''

FILE_TYPES = [
    'xlsx',
    'zip',
    'docx',
    'pdf',
    'csv',
    'pptx'
]

LOCAL_FILE_DIR = os.path.join(BASE_DIR, 'temp')