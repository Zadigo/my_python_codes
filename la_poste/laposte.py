import re
import os
import requests
from collections import namedtuple



BASE_URL   = 'https://api.laposte.fr/controladresse/v1/adresses?q={address}'

class Base:
    def __init__(self, secret_key='', *args):
        if not secret_key:
            environ_secret_key = os.environ.get('LA_POSTE_SECRET_KEY', None)

            if not environ_secret_key:
                raise KeyError('You have to provide a secret key.')

            else:
                self.secret_key = environ_secret_key
        
        else:
            self.secret_key = secret_key
        
    def create_request(self, uri):
        try:
            # Create the request with the mandatory headers
            response = requests.get(uri, headers={'X-Okapi-Key': self.secret_key})

        except requests.HTTPError as e:
            raise
        
        return response.json()

class CheckAdress(Base):
    def _check(self, address):
        """
        Check that the provided address exists and receives a dictionnary 
        if there are multiple addresses.

        The structure of the dictionnary is as follows:
        >>> {'0': {'code': '', 'adresse': ''}
        """
        uri = BASE_URL.format(address=address)
        return super().create_request(uri)

# a = CheckAdress('')
# a._check('36 rue de Suède 59120 Loos')

a='36 RUE DE SUEDE AVENUE LELIEVRE 59120 LOOS'
address = namedtuple('Address', ['street_number', 'street', 'postal_code', 'region'])

# e.g. 36
street_number = re.match(r'^(\d{1,3})\s+', a).group(0)
street = re.search(r'([A-Z\s+]+)\s+', a).group(0).strip()
postal_code = re.search(r'(\d{5})\s+', a).group(0).strip()
region = re.search(r'\s+([A-Z\-?]+)$', a).group(0).strip()

print(address(street_number,street,postal_code,region))