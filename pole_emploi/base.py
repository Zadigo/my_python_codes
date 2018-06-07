from importlib import import_module
from urllib.parse import urlencode

class  Base(type):
    def __new__(cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)

        try:
            settings = import_module('emploi_secret')
        except ImportError as error:
            print('Could not find module'
                '\'emploi_secret\' %s' % error.args)
            raise
        for key, setting in settings.__dict__.items():
            if key.isupper():
                setattr(new_class, key, setting)
        query = dict({
            'a': 'test'
        })
        request_url = urlencode(query)
        setattr(new_class, 'request_url', request_url)
        return new_class

class BaseEmploi(metaclass=Base):
    pass

class Emploi(BaseEmploi):
    def get_a(self):
        print(self.CLIENT_ID)