import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'name': 'volleyball',
    'aliases': []
}

IMAGES_PATH = os.path.join(BASE_PATH, 'images')

URI_DOMAIN = 'japan2018'

COUNTRY = 'rus-russia'

# URI_DOMAINS = ['japan2018']

# COUNTRIES = ['chn-china']

PLAYER_PAGE_URI = 'http://%(uridomain)s.fivb.com/en/competition/teams/%(country)s/players' % {
    'uridomain': URI_DOMAIN,
    'country': COUNTRY
}
