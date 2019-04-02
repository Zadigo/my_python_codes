from urllib.parse import urlencode
import requests
from datetime import datetime

BASE_URL = 'https://entreprise.pole-emploi.fr/connexion/oauth2/access_token'

CLIENT_ID = 'PAR_structureoffre_6f297f641c4187114336a7ae5523a47bb782c6877563e315c265fb754b0b9fbe'

CLIENT_SECRET = 'db79f5b51febd8d4a82cb461ecccbeecedfbd91470c36cd5b8503ffb73942bfd'


class PoleEmploi:
    def __init__(self):
        data = {
            'grant_type': 'client_credentials',
            'realm': '/partenaire',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'scope': 'application_%s %s' % (CLIENT_ID, 'api_pagesentreprisesv1'),
        }

        response = requests.post(BASE_URL, data)
        self.response = response.json()

    @property
    def access_token(self):
        return self.response['access_token']

    @property
    def expires_in(self):
        return datetime.fromtimestamp(self.response['expires_in']).time()
    
    @property
    def _bearer(self):
        return {
                'Authorization': 'Bearer %s' % self.access_token
            }

class PageEntreprise(PoleEmploi):
    def get_page(self, siret):
        url = f'https://api.emploi-store.fr/partenaire/pagesentreprises/v1/pagesentreprises/{siret}'
        bearer = 'Bearer %s' % super().access_token
        response = requests.get(url, headers={'Authorization': bearer})

# PoleEmploi()
# PageEntreprise().get_page('38012986646850')
