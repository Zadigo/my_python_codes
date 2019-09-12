import sqlite3
from games.bank.database.query import QuerySet, Manager
from collections import OrderedDict

TEST_PATH = 'C:\\Users\\Zadigo\\Documents\\Programs\\my_python_codes\\games\\bank\\database\\db.sqlite'


class Database:
    manager = Manager()

    def __init__(self, name=None, **kwargs):
        try:
            if not name:
                name = 'db.sqlite'
            db = sqlite3.connect(TEST_PATH, timeout=25)
        except sqlite3.DatabaseError:
            raise
        else:
            cursor = db.cursor()
            # Make the cursor and the database
            # available to the subclasses
            self.db = db
            self.cursor = cursor
            # Initialize the manager with
            # the database connection in order
            # to avoid using parameters
            # setattr(self.manager, 'cursor', self.cursor)
            manager_dict = self.manager.__dict__
            manager_dict.update(
                {
                    'cursor': self.cursor,
                    'db': self.db
                }
            )

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'Database(connected=True)'

    @property
    def connections(self):
        """Return the database connection parameters
        as a tuple

        Result
        ------
            (database.connection, database.cursor)
        """
        return self.db, self.cursor

    def tables(self):
        sql = """SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"""
        return self.manager._run_sql(sql)

# test = Database()
# test.tables()
# test.db.close()
