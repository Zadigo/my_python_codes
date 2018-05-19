import os
import time
import re
from collections import namedtuple
import googlemaps as gmaps
# try:
#     import googlemaps as gmaps
# except ImportError as error:
#     print('You should install Google maps API: "pip install googlemaps"')
#     raise

VILLES = [
    'Paris',
    'Nantes',
    'Roubaix, France',
    'Dunkerque'
]

BASE_DIR = os.path.dirname(__file__)



t=os.path.join(BASE_DIR,'secret.json')
print(t)

class GoogleMapsDistance:
    secret_key = None
    villes = []
    
    def __init__(self):
        if  self.secret_key is None:
            try:
                # Try to get key in environment
                self.secret_key = os.environ.get('GOOGLE_MAPS_KEY')
            except ValueError as error:
                print('You need to provide a secret key for the API: ' % GOOGLE_API_URL)
                raise
            else:
                # Try to get key on local
                self.secret_key = ''
            finally:
                pass

        else:
            print('Error')
            raise ValueError('There')

    def calculate_distance(self, origin='', destination='Lille', mode='driving', units='metric', **kwargs):
        distances = namedtuple('Distance', ['villes'])

        try:
            # Connect to API
            self._gmaps = gmaps.Client(key=self.secret_key)
        except gmaps.exceptions.ApiError as error:
            print('An error has occured %s' % error.args)
            raise

        try:
            result = self._gmaps.distance_matrix(origin, destination, mode, units)     
        except Exception as error :
            print('There was an error %s' % error.args)
            return distances({})  
        else:
            return distances(result)

print(GoogleMapsDistance().calculate_distance(origin='Roubaix'))