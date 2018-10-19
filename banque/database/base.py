import sqlite3 as db
from collections import OrderedDict

class Descriptor:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

class BaseDatabase(type):
    def __new__(cls, clsname, bases, clsdict):
        try:
            # Create database instance
            conn = db.connect('data.db')
            cursor = conn.cursor()
        except db.DatabaseError as error:
            print('Could not connect to database %s' %error.args)
            raise
        else:
            clsdict['cursor_object'] = cursor
        new_class = super().__new__(cls, clsname, bases, clsdict)
        return new_class

class Database(metaclass=BaseDatabase):
    pass

class BaseManager(Database):
    pass

a = BaseManager()
# print(BaseManager.__dict__)
print(a.cursor_object)
