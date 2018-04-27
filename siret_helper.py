import re
from datetime import datetime
from collections import namedtuple
import requests as req

URL = u'https://data.opendatasoft.com/api/records/1.0/search/?dataset=sirene%40public&q={siren}'

class CheckSiret(object):    
    def _check(self, siret_number):
        if siret_number is None or siret_number == '' or siret_number == 0:
            # return False, 'Vous evez entrer un nuéro %s' % (siret_number)
            raise TypeError('There was nothing in SIRET')

        number_length = re.search(r'[0-9]{14}', str(siret_number))
        if number_length is None:
            # return False, 'Vous n\'avez pas entrez 15 nuéro %s' % (siret_number)
            raise TypeError('Vous n\'avez pas entrez 15 nuéro %s' % (siret_number)) 

        return str(siret_number)



def get_enterprise(siret):
    errors = []
    return_value = CheckSiret()._check(siret)
    if not return_value[0]:
        errors.append(return_value)
        return errors

    try:
        response = req.get(URL.format(siren=siret))
        # assert response != 200, 'T'
        
    except ConnectionAbortedError as error:
        return 't'

    else:
        get_json_object = response.json()
        # assert get_json_object is not None
        get_records = get_json_object['records']
        # assert get_records is not None

        entre = namedtuple('Entreprise', ['records', 'created_at'])

        try:
            create_dict = dict(
                l1_declaree=get_records[0]['fields']['l1_declaree'],
                nom_dept=get_records[0]['fields']['nom_dept'],
                activite=get_records[0]['fields']['section'],
                categorie=get_records[0]['fields']['categorie']
            )

        except IndexError:
            return None

        else:
            return entre(create_dict, datetime.now)

        # return create_dict

print(get_enterprise(44146037500088))


# a = ur.format(siren='44146037500088')

# response = req.get(a)
# a = response.json()
# b = a['records']

# w = dict(
#     l1_declaree=b[0]['fields']['l1_declaree'],
#     nom_dept=b[0]['fields']['nom_dept'],
#     activite=b[0]['fields']['section'],
#     categorie=b[0]['fields']['categorie']
# )
# print(w)