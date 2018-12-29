from dataclasses import dataclass
import sqlite3
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'name': 'volleyball',
    'aliases': []
}

class QuerySelector(DatabaseModel):
    def _update(self, table='players', columns=(), values=()):
        sql = f"INSERT INTO {table}{columns} VALUES {values};"
        print(sql)
        # self._meta._cursor(sql)

class Options:
   def __init__(self, meta=''):
        database_path = os.path.join(BASE_PATH, DATABASES['name'] + '.sqlite')
        connection = sqlite3.connect(database_path)

        self._db = connection
        self.database_name = '%s.sqlite' % DATABASES['name']
        self._cursor = connection.cursor().execute

class BaseDatabase(type):
    def __new__(cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)

        # Create class
        setattr(new_class, '_meta', Options())

        return new_class

class Database(metaclass=BaseDatabase):
    def auto_migrate(cls, *args):
        new_table = """
        CREATE TABLE players(
            player_id INTEGER PRIMARY KEY,
            player_name CHAR(100),
            player_surname CHAR(100),
            profile_link CHAR(250),
            site_id INTEGER
        );
        """
        try:
            cls._meta._cursor(new_table)
        except sqlite3.OperationalError as e:
            raise

class DatabaseModel(Database):
    def _save(self, cursor, commit=False):
        # a=sqlite3.connect('a.sqlite')
        # a.cursor().execute('').save()
        pass

DatabaseModel()._save()



    # def _aliases(self):
    #     databases=[]
    #     if DATABASES['aliases']:
    #         for alias in DATABASES['aliases']:
    #             paths = os.path.join(BASE_PATH, alias + '.sqlite')
    #             databases.append(sqlite3.connect(alias).cursor())
    #     return databases


# QuerySelector()._update('test','a',('a','c'))

# QuerySelector()._update(columns=('a','c'),values=('a','c'))