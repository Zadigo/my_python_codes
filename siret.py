import re
import requests as req
from datetime import datetime
from collections import namedtuple

class BaseCheckSiret:
    fields = ['l1_declaree', 'nom_dept', 'section', 'categorie']
    verification_url = u'https://data.opendatasoft.com/api/records/1.0/search/?dataset=sirene%40public&q={siren}'
    
    @staticmethod
    def check(siret):
        if not isinstance(siret, int):
            raise TypeError('Vous devez entrer un numéro: %s' % (siret,))

        number_length = re.search(r'[0-9]{14}', str(siret))
        if number_length is None:
            raise TypeError('Vous devez avoir un numéro 15 chiffres au lieu de %s' % (siret,))

        return number_length.group(0)

    def get_entreprise(self, siret):
        """
        Use this module to check that the SIRET
        of an enterprise exists and get the
        informations related to that entreprise
        in a json format style
        """

        entreprise = namedtuple('Entreprise', ['records', 'created_at'])
        self.check(siret)
        try:
            response = req.get(self.verification_url.format(siren=siret))
        except ConnectionAbortedError as error:
            print('There was an error: %s' % error.args)
            raise
        else:
            if response.status_code == 200:
                json_object = response.json()
                records     = json_object['records'][0]['fields']
                search      = []
                for field in self.fields:
                    search.append(records[field])

                return entreprise(search, datetime.now())

class CheckSiret(BaseCheckSiret):
    """
    Use this class for subclassing
    """

class A(CheckSiret):
    pass

a = A()
print(a.get_entreprise(51177973800042))