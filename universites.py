import re
from datetime import datetime
from collections import namedtuple
import requests as req

URL = u'https://data.opendatasoft.com/api/records/1.0/search/?dataset=fr-esr-principaux-diplomes-et-formations-prepares-etablissements-publics%40mesr&sort=-rentree_lib&refine.diplome_rgp=Master&refine.discipline_lib=Sciences+%C3%A9conomiques%2C+gestion&timezone=Europe%2FBerlin'

def get_universites():
    try:
        response = req.get(URL)
        # assert response != 200, 'T'
        
    except ConnectionAbortedError as error:
        return 't'

    else:
        get_json_object = response.json()
        # assert get_json_object is not None
        get_records = get_json_object['records'][0]['fields']
        # assert get_records is not None

        universites = namedtuple('Universites', ['records', 'created_at'])

        try:
            for record in get_records:
                create_dict = dict(
                    gd_disciscipline_lib=get_records['gd_disciscipline_lib'],
                    etablissement_type=get_records['etablissement_type'],
                    libelle_intitule_2=get_records['libelle_intitule_2'],
                    diplome_rgp=get_records['diplome_rgp'],
                    libelle_intitule_1=get_records['libelle_intitule_1'],
                )

        except IndexError:
            return None

        else:
            return universites(create_dict, datetime.now())

print(get_universites())