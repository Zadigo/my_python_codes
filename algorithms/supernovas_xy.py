import sqlite3
import os
import itertools

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DATABASE = {
    'name': 'test',
}

class Options:
    def __init__(self, meta):
        database_name = '.'.join([DATABASE['name'], 'sqlite'])
        database_path = os.path.join(BASE_PATH, database_name)

        db = sqlite3.connect(database_path)
        cursor = db.cursor()

        self.database_name = database_name or None
        self.verbose_name = None
        self.object_name = None
        self.meta = meta
        self._cursor = cursor.execute

class BaseDatabase(type):
    def __new__(cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)

        # Création de la classe
        new_class.add_to_class('_meta', Options('test'))

        return new_class

    def add_to_class(cls, name, value):
        setattr(cls, name, value)

class A(metaclass=BaseDatabase):
    pass

class C(A):
    def _test(self):
        pass

# print(C.__dict__)


print(tuple(itertools.chain('are',[1,2])))