import sqlite3 as db
import configuration

class Base(type):
    def __new__(cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)
        setattr(new_class, 'get_database', configuration.PATHS['database'])
        return new_class

class BaseDatabase(metaclass=Base):
    pass

class Database(BaseDatabase):
    pass
