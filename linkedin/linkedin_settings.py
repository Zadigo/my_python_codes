import string
import random
from urllib.parse import urlencode
import os
from importlib import import_module
import re

def _generator():
    chars = string.ascii_letters + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(15))

LINKEDIN_CLIENT_ID = ''

LINKEDIN_CLIENT_SECRET = ''

ACCESS_TOKEN_LINK = 'https://www.linkedin.com/oauth/v2/{accessToken}'

AUTH_LINK = 'https://www.linkedin.com/oauth/v2/authorization?'

AUTH_TOKEN = urlencode({
    'grant_type': 'authorization_code',
    'code': 'code',
    'redirect_uri': 'http://www.kurrikulam.com/accounts/profile',
    'client_id': LINKEDIN_CLIENT_ID,
    'client_secret': LINKEDIN_CLIENT_SECRET
})

AUTH_QUERY = urlencode({
    'response_type': 'code',
    'client_id': LINKEDIN_CLIENT_ID,
    'redirect_uri': 'http://www.kurrikulam.com/accounts/profile',
    'state': _generator(),
    'scope': 'r_basicprofile'
})

class Settings:
    def __init__(self):
        self.path = os.path.abspath(__file__)
        settings = []
        module = import_module('linkedin_settings')
        items = module.__dict__
        for item, value in items.items():
            if str(item).isupper():
                setattr(self, item, value)