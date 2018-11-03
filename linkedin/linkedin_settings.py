import string
import random
from urllib.parse import urlencode
import os
from importlib import import_module
import re

CLIENT_ID = ''

CLIENT_SECRET = ''











def _generator():
    chars = string.ascii_letters + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(15))


# ACCESS_TOKEN_LINK = 'https://www.linkedin.com/oauth/v2/{accessToken}'

# AUTH_LINK = 'https://www.linkedin.com/oauth/v2/authorization?'

# AUTH_TOKEN = {
#     'grant_type': 'authorization_code',
#     'code': 'code',
#     'redirect_uri': 'http://www.kurrikulam.com/accounts/profile',
#     'client_id': LINKEDIN_CLIENT_ID,
#     'client_secret': LINKEDIN_CLIENT_SECRET,
#     'x-li-format': 'json'
# }

# AUTH_QUERY = urlencode({
#     'response_type': 'code',
#     'client_id': LINKEDIN_CLIENT_ID,
#     'redirect_uri': 'http://www.kurrikulam.com/accounts/profile',
#     'state': _generator(),
#     'scope': 'r_basicprofile'
# })

# class Settings:
#     def __init__(self):
#         self.path = os.path.abspath(__file__)
#         settings = []
#         module = import_module('linkedin_settings')
#         items = module.__dict__
#         for item, value in items.items():
#             if str(item).isupper():
#                 setattr(self, item, value)


# USER_AGENTS = [
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
#         "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#         "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
#     ]



# # HEADERS = {
# #     'client_id': LINKEDIN_CLIENT_ID,
# #     'client_secret': LINKEDIN_CLIENT_SECRET,
# # }

# PEOPLE_LINK = 'https://api.linkedin.com/v1/people/~?format=json'