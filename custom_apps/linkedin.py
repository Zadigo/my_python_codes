import requests
import random
import string
from urllib.parse import urlencode


AUTH_URL = 'https://www.linkedin.com/oauth/v2/authorization'
ACCESS_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
CLIEN_ID = ''
SECRET_KEY = ''
redirect_uri = 'https://www.example.com/'

def state_generator(chars=string.ascii_lowercase+string.ascii_uppercase, size=20):
    return ''.join(random.choice(chars) for _ in range(size))

class LinkedIn:
    def __init__(self, *args, **kwargs):
        self.auth_url = AUTH_URL
        # try:
        #     response = requests.get(url, headers=headers)
        # except requests.HTTPError as error:
        #     print(error.args)
        # print(response)

    def client(self, client_id, redirect_uri, state=state_generator(), response_type='code', scope='r_basicprofile'):
        print(state)
        query = {
            'response_type':response_type,
            'client_id':client_id,
            'redirect_uri':redirect_uri,
            'state':state,
            'scope':scope,
        }
        self.auth_url += '?' + urlencode(query)
        try:
            response = requests.get(self.auth_url)
        except requests.HTTPError as error:
            print(error.args)
            raise

        p = {
            'grant_type':'authorization_code',
            'code':response,
            'redirect_uri':'redirect_uri',
            'client_id':client_id,
            'client_secret':'VLkvO0P7JTJacuDd',
        }
        try:
            a = requests.post(self.auth_url, data=p)
        except requests.HTTPError as error:
            print(error.args)
            raise
        
        print(a)


LinkedIn().client('eezezrgrrger', '')