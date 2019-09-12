# import urllib
# import requests

# BASE_URL = 'https://api-adresse.data.gouv.fr/search/?'

# class CheckAddress:
#     query = {}
#     def __init__(self, address, limit=0, postcode=0):
#         self.query['q'] = address
#         if limit != 0 or postcode != 0:
#             self.query['limit'] = address
#             self.query['postcode'] = postcode

#         _enc_query = urllib.parse.urlencode(self.query)

#         try:
#             self._response = requests.get(BASE_URL + _enc_query)
#         except ConnectionError as error:
#             print('There was an unknown error. %s' %
#              error.args)

#     @property
#     def get_address(self):
#         return self._response.json()['features']

    # def curry(self):
    #     addresses = self.get_address
    #     results = []
    #     for key, address in addresses.items():
    #         results.append(address) if key == 'features'
