import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = {
    'secret_path': os.path.join(BASE_DIR, 'secret.json'),
    'secret_env': os.environ.get('MAPS_SECRET_KEY'),
    'secrets': [
        
    ]
}
