import datetime
import requests as req
from collections import namedtuple
from urllib.parse import urljoin, urlencode
# import emploi_secret

query = {
    'realm': '%2Fpartenaire',
    'grant_type': 'client_credentials',
    'client_id': '',
    'client_secret': '',
    'scope': 'application_%s %s' % ('client_id', 'api_pagesentreprisesv1'),
}

print(urlencode(query))

# # _TOKEN = namedtuple('Accesstoken', ['value', 'expiration'])
# access_tokens = {}

# # 1- Better way to construct URI to generate toen ??????
# BASE_URI = 'https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?'
# REALM = '&realm=%2Fpartenaire'
# grant_type = '&grant_type=client_credentials'
# client_id = 'PAR_structureoffre_892b4316f9e7203cb20b9ad4ae13bb11f5186fa627ac67e1a22ca014929a16b3'
# client_secret = '&client_secret=425fc099c995e2260e691a09a42b6217d9f27fbbb5f9aeeb0c8aa63202e818c2'
# SCOPE = 'scope=application_%s %s' % (client_id, 'api_pagesentreprisesv1')
# POST_URI = BASE_URI + REALM + grant_type + '&client_id=' + client_id + client_secret + '&' + SCOPE

# def _generate_token():
#     auth_request = req.post(POST_URI)
#     response = auth_request.json()
#     token = response['access_token']
#     # expires_in = datetime.timedelta(seconds=response['expires_in'])
#     # access_tokens[scope] = _TOKEN(token, expires_in)
#     return token


# # {'scope': 'application_PAR_structureoffre_892b4316f9e7203cb20b9ad4ae13bb11f5186fa627ac67e1a22ca014929a16b3 api_pagesentreprisesv1', 'expires_in': 1499, 'token_type': 'Bearer', 'access_token': 'b3b0af7b-9c8d-4949-9a71-d8afc15f5477'}

# # 2- Call API

# API_URI = 'https://api.emploi-store.fr/partenaire'
# a = 'https://api.emploi-store.fr/partenaire/pagesentreprises/v1/pagesentreprises/{siret}'.format(siret=44146037500088)

# entreprise = req.get(a, headers={'Authorization': 'Bearer %s' % _generate_token()})
# print(entreprise.text)