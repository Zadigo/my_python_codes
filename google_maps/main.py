import os
import time
import googlemaps as gmaps
from collections import namedtuple
from secret import get_secret

VILLES = [
    'Paris',
    'Nantes',
    'Roubaix, France',
    'Dunkerque'
]

class Mixins:
    pass


class GoogleMapsDistance(Mixins):
    secret_key = None
    villes = []
    
    def __init__(self):
        if  self.secret_key is None:
            try:
                # Try to get key on local
                self.secret_key = get_secret()
            else:
                # Try to get key in environment
                self.secret_key = os.environ.get('GOOGLE_MAPS_KEY')
            except KeyError as error:
                print('You need to provide a secret key for the API: ' % GOOGLE_API_URL)
                raise

        else:
            pass

        try:
            self._gmaps = gmaps.Client(key=self.secret_key)
        except gmaps.exceptions.ApiError as error:
            print('An error has occured %s' % error.args)
            raise

    def calculate_distance(self, origin='', destination='Lille', mode='driving', units='metric', **kwargs):
        distances = namedtuple('Distance', ['villes'])

        try:
            result = self._gmaps.distance_matrix(origin, destination, mode, units)     
        except Exception as error :
            print('There was an error %s' % error.args)
            return distances({})  
        else:
            return distances(result)

# print(GoogleMapsDistance().calculate_distance(origin='Roubaix'))
