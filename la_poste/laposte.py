import re
import os
import requests
from collections import namedtuple

class LaPosteAPI:
    """This API uses La Poste's address verification
    service in order to determine wheter an address
    exists or not.
    """
    secret_key = 'mzNxDiEp9BKgrW5LItSTjoYzbRHTjXLtmE0rc7cfa8FUus+B4lCaF8r+cyVRdDUW'

    def create_request(self, url, *args):
        """Create an API request to La Poste.
        """
        # Try to get secret key in the
        # environment if it was not provided
        if not self.secret_key:
            environ_secret_key = os.environ.get('LA_POSTE_SECRET_KEY', None)

            if not environ_secret_key:
                raise KeyError('You have to provide a secret key.')
            else:
                self.secret_key = environ_secret_key
                
        try:
            # Create the request with the mandatory headers
            response = requests.get(url, headers={'X-Okapi-Key': self.secret_key})
        except requests.HTTPError:
            raise
        else:
            return response.json()

class CheckAdress(LaPosteAPI):
    """
    Check that the provided address exists and receive a dictionnary 
    if there are multiple addresses.

    The structure of the dictionnary is as follows:
    >>> {'0': {'code': '', 'adresse': ''}
    """
    def __init__(self, address):
        self.response = self.create_request(
            'https://api.laposte.fr/controladresse/v1/adresses?q={address}'.format(address=address)
        )

    def __str__(self):
        return str(self.response)



# a='36 RUE DE SUEDE AVENUE LELIEVRE 59120 LOOS'
a='36 BIS RUE DE SUEDE 37100 TOURS'

z=re.search(r'^(\d+)\s+((?:\w+\s+)+(?=\d+))(\d+)\s+(.*)$', a)
n=z.group(1)
rue=z.group(2)
cp=z.group(3)
ville=z.group(4)
print(ville)

# print(CheckAdress('36 RUE DE SUEDE'))