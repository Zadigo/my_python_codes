import re
import requests as req
from datetime import datetime
from collections import namedtuple

VERIFICATION_URL = u'https://data.opendatasoft.com/api/records/1.0/search/?dataset=sirene%40public&q={siren}'


class CheckSiret:
    def check(self, siret):
        if not isinstance(siret, int):
            raise TypeError('Vous devez entrer un numéro: %s' % (siret,))

        number_length = re.search(r'[0-9]{14}', str(siret))
        if number_length is None:
            raise TypeError('Vous devez avoir un numéro 15 chiffres au lieu de %s' % (siret,))

        return number_length.group(0)

def request_decorator(function):
    entreprise = namedtuple('Entreprise', ['records', 'created_at'])

    def request_object(self, siret):
        try:
            response = req.get(VERIFICATION_URL.format(siren=siret))
        except ConnectionAbortedError as error:
            print('%s' % error.args)
            raise
        else:
            if response.status_code == 200:
                json_object = response.json()
                records     = json_object['records'][0]['fields']
                fields      = function(self, siret)
                search=[]
                for field in fields:
                    search.append(records[field])

                return entreprise(search, datetime.now())
            else:
                return []
    return request_object

@request_decorator
def c(r,siret):
    return ['l1_declaree', 'nom_dept', 'section', 'categorie']

@CheckSiret.check(CheckSiret, siret=44146037500088)
def t():
    return 'r'

print(t())
