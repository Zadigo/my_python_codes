import json
import os
import re
import time
from collections import namedtuple

import googlemaps as gmaps
# from maps_settings import SECRET_KEY
# from utils import create_cache

class Maps:
    secret_key = None

    def __init__(self):
        try:
            self._connection = gmaps.Client(key=self.secret_key)
        except gmaps.exceptions.HTTPError as e:
            raise
        
    def load_keys_from_file(self, path):
        if os.path.exists(path):
            with open(path, mode='r', encoding='utf-8') as secret_file:
                secret_file_keys = json.load(secret_file)

                if 'secret' in secret_file:
                    self.secret_key = secret_file_keys['secret']

class DistanceCalculator(Maps):
    def _raw(self, origin, destination, mode, units):
        return self._connection.distance_matrix(origin, destination, mode, units)

# class StartMaps:
#     def __init__(self):
#         secret = ''
#         if os.path.exists(SECRET_KEY['secret_path']):
#             with open(SECRET_KEY['secret_path'], mode='r', encoding='utf-8') as secret_file:
#                 secret_file_dict = json.load(secret_file)

#                 if 'secret' in secret_file_dict:
#                     secret = secret_file_dict['secret']

#         else:
#             if SECRET_KEY['secret_env'] is not None:
#                 secret = SECRET_KEY['secret_env']

#             else:
#                 print(SECRET_KEY['secrets'])
#         #         for key in SECRET_KEY['secrets']:
#         #             print(key)
#         #             if key:
#         #                 secret = key
#         #                 quit()
#         # print(secret)

#         # if not secret or secret is None:
#         #     raise KeyError('We could not find a secret key. Did you forget to get one from Google API?')

#         # Connect to API
#         try:
#             self._connection = gmaps.Client(key=secret)
#         except gmaps.exceptions.HTTPError as e:
#             print('There was an error trying to connect to : %s' % e.args)
#             raise

#         # self.c = create_cache(self._connection, secret)
        

# class DistanceCalculator(StartMaps):
#     def _raw(self, origin, destination, mode, units):
#         return self._connection.distance_matrix(origin, destination, mode, units)

#     def get_distance(self, origin, destination, mode, units):
#         return self._raw(origin, destination, mode, units)
