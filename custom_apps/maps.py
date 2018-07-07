import os
import time

import googlemaps as gmaps

from collections import namedtuple

from django.conf import settings

class BaseGoogleMaps:
    secret_key = settings.GOOGLE_MAPS_SECRET_KEY
    
    def __init__(self, request='', *args, **kwargs):
        if self.secret_key is None or self.secret_key == '':
            raise KeyError('You need to provide a secret'
            'key for the API')

        try:
            self._gmaps = gmaps.Client(key=self.secret_key)
        except gmaps.exceptions.ApiError as error:
            print('Could not connect to API: %s' % error.args)
            raise

class CalculateDistance(BaseGoogleMaps):
    def CalculateDistance(self, origin='', destination='Lille', mode='driving', units='metric', **kwargs):
        distance = namedtuple('Distance', ['informations'])

        try:
            result = self._gmaps.distance_matrix(origin, destination, mode, units)
        except gmaps.exceptions.ApiError as error:
            print('There was an error %s' % error.args)
            return distance({})
        else:
            return distance(result)