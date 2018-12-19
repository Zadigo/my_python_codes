import sqlite3
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'name': 'volleyball',
    'aliases': []
}


class Database:
    def __init__(self):
        database_path = os.path.join(BASE_PATH, DATABASES['name'] + '.sqlite')
        connection = sqlite3.connect(database_path)
        self.cursor = connection.cursor()

    # def _aliases(self):
    #     databases=[]
    #     if DATABASES['aliases']:
    #         for alias in DATABASES['aliases']:
    #             paths = os.path.join(BASE_PATH, alias + '.sqlite')
    #             databases.append(sqlite3.connect(alias).cursor())
    #     return databases


class Migrator(Database):
    def auto_migrate(self, *args):
        players_table_sql = """
        CREATE TABLE players(
            player_id INTEGER PRIMARY KEY,
            player_name CHAR(100),
            player_surname CHAR(100),
            profile_link CHAR(250),
            site_id INTEGER
        );
        """
        self.cursor.execute(players_table_sql)


class QuerySelector:
    def _update(self, table, columns, values=()):
        sql = "INSERT INTO {table} ({columns}) VALUES {values};".format(
            table=table,
            columns=columns,
            values=values
        )
        print(sql)
        # self.cursor.execute(sql)

QuerySelector()._update('test','a',('a','c'))