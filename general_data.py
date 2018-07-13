import importlib
import re
import datetime

ADRESSE_EDITEUR = '20 rue du Docteur Calmette, Loos'

ADRESSE_ENTREPRISE = '20 rue du Docteur Calmette, Loos'

ADRESSE_HEBERGEUR = '2 rue Kellermann 59100 - Roubaix'

CURRENT_YEAR = datetime.datetime.now().year

MAIL_ENTREPRISE = 'pendenquejohn@gmail.com'

NOM_ENTREPRISE = 'Kurrikulam'

NOM_EDITEUR = 'John PENDENQUE'

NOM_HEBERGEUR = 'OVH'

NOM_SITE = 'Kurrikulam'

SITE = ''

SIREN = ''

SIRET = ''

SOCIAL_TWITTER = ''

SOCIAL_FACEBOOK = ''

SOCIAL_LINKEDIN = ''

SOCIAL_INSTAGRAM = ''

TELEPHONE_EDITEUR = '0668552975'

TVA = 20

URI_ANNULER_RECEP_OFFRE_CO = 'http://www.example.com/annuler'

URI_CNIL = 'https://www.cnil.fr/'

URI_CNIL_COOKIES_LOI = 'https://www.cnil.fr/fr/cookies-traceurs-que-dit-la-loi'

URI_CNIL_COOKIES_CONSEIL = 'https://www.cnil.fr/fr/cookies-les-outils-pour-les-maitriser'

# API SECRET

SECRET_LAPOSTE = ''

SECRET_MAPS = ''

SECRET_LINKEDIN = ''

SECRET_STRIPE = ''

SECRET_SHEETS = ''

SECRET_GMAIL = ''


# Class

PATTERNS = {
    'secret':r'SECRET\_[\w+\_]+',
    'social': r'SOCIAL\_[\w+\_]+'
}

class GeneralDataDictionnary:
    def __init__(self, secret=False):
        self._items = {}
        try:
            this_module = importlib.import_module('general_data').__dict__
        except ImportError:
            print('The module was not found.' 
                    'Did you change its name? %s' % os.path.basename(__file__))
            raise
        for k, v in this_module.items():
            self._items[k] = v
    
    @property
    def get_all(self):
        return self._items

    @property
    def get_secret(self):
        secret = {}
        for k, v in self._items.items():
            s = re.search(PATTERNS['secret'], k)
            if s is not None:
                secret[k] = v
        return secret

    @property
    def get_social(self):
        social = {}
        for k, v in self._items.items():
            s = re.search(PATTERNS['social'], k)
            if s is not None:
                social[k] = v
        return social

# Autodetect module name
# import os
# a = os.path.basename(__file__)
# base, ext = str(a).rsplit('.')
# importlib.import_module(base)