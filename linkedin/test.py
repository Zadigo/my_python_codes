from linkedin_settings import CLIENT_ID, CLIENT_SECRET, _generator
from oauthlib.oauth2 import Client, WebApplicationClient, BearerToken, AuthorizationCodeGrant
from oauthlib.common import Request

# client = WebApplicationClient(CLIENT_ID)
# url = client.prepare_request_uri('https://www.example.com', state=_generator())
# print(url)

request = Request('https://www.example.com', http_method='GET', headers='', body=None)
token = BearerToken(CLIENT_ID)
grant = AuthorizationCodeGrant(CLIENT_ID)
grant.create_authorization_response(request, token)