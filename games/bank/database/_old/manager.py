import sqlite3

from games.bank.database.migrator import Database
from games.bank.database.fields import IntegerField
from games.bank.settings.configuration import DATABASE
from games.bank.database.fields import CharField, IntegerField

try:
    import psycopg2
except ImportError:
    pass



class Options:
    """Class that adds additional meta values to
    a database class and extends some of its functionnalities
    in that regards
    """
    database = None

    def __init__(self, *args, **kwargs):
        if 'database' in kwargs:
            self.database = kwargs['database']

class BaseModel(type):
    def __new__(cls, cls_name, bases, cls_dict):
        super_new = super().__new__
        new_class = super_new(cls, cls_name, bases, cls_dict)
        # Add additional meta values to the
        # database class that we are using
        options = Options(database='Person')
        new_class.add_to_class('_meta', options)

        # Get the classes fields
        if cls_name != 'Model':
            fields = []
            for name, field in cls_dict.items():
                if isinstance(field, (IntegerField)):
                    fields.append(field)
            print(fields)

        return new_class

    def add_to_class(cls, name, value):
        """A helper function that sets attributes
        for a given class
        """
        setattr(cls, name, value)

class Model(metaclass=BaseModel):
    # def __init__(self):
        # self.db_connection = self.connect()
        # pass

    connection = Database()

    def save(self):
        pass

    def pre_save(self):
        pass

    def post_save(self):
        pass

    def refresh(self):
        pass

    @staticmethod
    def connect():
        default_database = DATABASE['default']
        try:
            if DATABASE['default']['ENGINE'] == 'sqlite':
                conn = self.connection[0].
            else:
                conn = psycopg2.connect(**DATABASE['default'])
        except ConnectionError:
            pass
        else:
            if conn:
                cursor = conn.cursor
                return cursor
            else:
                return None
