import sqlite3 as db
from migrator import DatabaseMigrator

class MainManager(type):
    def __new__(cls, name, bases, cls_dict):
        new_class = super().__new__(cls, name, bases, cls_dict)
        return new_class

class MainManagerBase(metaclass=MainManager):
    pass

class MainDatabase(MainManagerBase, DatabaseMigrator):
    def __init__(self):
        try:
            print('We try to connect to the database')
            self.database = db.connect('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/banque_database/db.sqlite')
        except db.Error as e:
            print('Was not able to find database db.sqlite')
            raise
        else:
            pass

        print('We then migrate the different settings of the application')

    @property
    def _connection(self):
        return self.database

    @property
    def _cursor(self):
        return self.database.cursor()

# class DatabaseActions(MainDatabase):
#     pass

# class UpdateRecord(DatabaseActions):
#     def update_record(self, value, table, fields):
#         connection = self.database
#         sql = 'UPDATE {values} FROM {table} WITH {fields}'

w = MainDatabase()._cursor
print(w)