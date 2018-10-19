import requests
from linkedin_settings import LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET, AUTH_QUERY, AUTH_TOKEN, AUTH_LINK

a = 'https://www.linkedin.com/oauth/v2/authorization?'

GET_ACCESS_TOKEN_LINK = 'https://www.linkedin.com/oauth/v2/{accessToken}'

authorizatio_query = {
    'response_type': 'code',
    'client_id': LINKEDIN_CLIENT_ID,
    'redirect_uri': 'http://www.kurrikulam.com/accounts/profile',
    'state': generator(),
    'scope': 'r_basicprofile'
}

b = urllib.parse.urlencode(authorizatio_query)

def connect_linkedin(request, code, state):
    # Get authorization
    if state == authorizatio_query['state']:
        GET_ACCESS_TOKEN_LINK.format(code)
        # Generate token
        access_token_query = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://www.kurrikulam.com/accounts/profile',
            'client_id': LINKEDIN_CLIENT_ID,
            'client_secret': LINKEDIN_CLIENT_SECRET
        }
        # Use token
        _requests()

def _requests(url, headers={}, **kwargs):
    if headers:
        if 'access_token' in kwargs:
            headers.update({'Bearer': kwargs['access_token']})

    return requests.get(url, headers)

