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

COUNTRIES_PATH = ''

COUNTRIES = [
    'arg-argentina',
    'aze-azerbaijan',
    'bra-brazil',
    'bul-bulgaria',
    'cmr-cameroon',
    'can-canada',
    'chn-china',
    'cub-cuba',
    'dom-dominican%20republic',
    'ger-germany',
    'ita-italy',
    'jpn-japan',
    'kaz-kazakhstan',
    'ken-kenya',
    'kor-korea',
    'mex-mexico',
    'ned-netherlands',
    'pur-puerto%20rico',
    'rus-russia',
    'srb-serbia',
    'tha-thailand',
    'tto-trinidad%20%20tobago',
    'tur-turkey',
    'usa-usa'
]

COUNTRY_CODES = {
    'china': 1,
    'usa': 2
}

PLAYER_PAGE_URI = 'http://%(uridomain)s.fivb.com/en/competition/teams/%(country)s/players' % {
    'uridomain': URI_DOMAIN,
    'country': COUNTRY
}

def team_pages():
    for c in COUNTRIES:
        uri = f'http://{URI_DOMAIN}.fivb.com/en/competition/teams/{c}/players'
        yield uri

team_pages()