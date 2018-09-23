import sqlite3 as db
from migrator import BaseMigrator

class MainManagerBase(type):
    def __new__(cls, name, bases, cls_dict):
        new_class = super().__new__(cls, name, bases, cls_dict)
        return new_class

class MainManager(metaclass=MainManagerBase):
    pass

class Manager(MainManager, BaseMigrator):
    """
    This is the main manager for the local database. It connects 
    to the database and then returns the cursor.

    The manager contains elements from the migrator class.
    """
    def __init__(self):
        try:
            print('-'*10 + '>', 'We try to connect to the database')
            # self.database = db.connect('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/banque_database/db.sqlite')
            self.database = db.connect('D:\\Programs\\Python\\repositories\\python_codes\\Games\\Banque\\banque_database\\db.sqlite')
        except db.Error:
            print('Was not able to find database db.sqlite')
            raise
        else:
            pass

        print('-'*10 + '>', 'We then migrate the different settings of the application')
        Klass = BaseMigrator(self.database, commit=True)
        

    @property
    def _connection(self):
        return self.database

    @property
    def _cursor(self):
        return self.database.cursor()

w = Manager()._cursor
# print(w)
