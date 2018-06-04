import requests as req
import re
from collections import namedtuple
from global_settings import LA_POSTE_SECRET_KEY

BASE_URL   = 'https://api.laposte.fr/controladresse/v1/adresses?q={adress}'

class CheckAdress:
    secret_key = LA_POSTE_SECRET_KEY
    def __init__(self, adress):
        self.REQUEST_URL = BASE_URL.format(
            adress=adress
        )
        if  not self.secret_key:
            raise TypeError(' There was not secret key')
        try:
            self.auth_request  = req.get(
                BASE_URL,
                headers={'X-Okapi-Key': self.secret_key
                }
            )
        except ConnectionError as error:
            print('There was an error connecting'
                    'to the API %s' % error.args)
    
    @property
    def get_adress(self):
        """
        Returns a searched adress
        regardless of the number
        of adresses in the list
        """
        return self.auth_request.json()

    def multiple_adresses(self):
        s = namedtuple('Adresses', ['Result'])
        adresses = self.get_adress
        results = []
        for adress in adresses.items():
            adress_detail = adress[1]['adresse']
            results.append(adress_detail)
        return results

    @classmethod
    def regex_adress(cls, adress):
        patterns = [
            # e.g. 13646
            r'[0-9]{4}',
            # e.g. 1 RUE NICOLAS COPERNIC
            r'(\d+\s+[A-Z\s+]+)\s+[0-9]{4,5}',
            # e.g. ARLES
            r'[0-9]{4,5}\s+([A-Z]+)'
            # e.g. BOISSY ST LEGER CEDEX
            r'[0-9]{4,5}\s+([A-Z\s+]+)\s+CEDEX'
        ]
        pass
        # e = 'SARL ADRESS 1 RUE NICOLAS COPERNIC 13646 ARLES CEDEX'
        # code_postal = re.search()


print(CheckAdress('20 rue du Docteur Calmette 59120 Loos').get_adress)
