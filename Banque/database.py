import re
import setting_conf
import sqlite3 as db
import os
from context_builder import ContextBuilder


class DatabaseMixins:
    order       = None
    table_name  = None


class BaseDatabase(DatabaseMixins):
    def __init__(self, *args, **kwargs):
        self.context = ContextBuilder(self).get_context_object()

    def get_cursor(self):
        try:
            # Connect to database, 
            conn = db.connect(setting_conf.DATABASE['default']['path'])

        except Exception as error:
            print('There was an error. %s' % error.args )
            raise
        
        with conn:
            cursor = conn.cursor()
            return cursor

class DatabaseQueries(BaseDatabase):
    SQL         = None

    def get_user(self, **kwargs):
        if 'username' not in kwargs:
            raise TypeError('there')

        SQL = 'SELECT * FROM User_Model WHERE user_name=?'
        records = super().get_cursor().execute(SQL, (kwargs.get('username'),))

        # Append record to context
        self.context.update_context(query=records)
        
        return list(records) or []

a=DatabaseQueries()
a.get_user(username='a')



#     def select_all(self, *args, **kwargs):
#         if 'table_name' in kwargs:
#             self.table_name = kwargs.get('table_name')

#         SQL = 'SELECT * FROM ' + self.table_name

#         records = super()._cursor().execute(SQL)
#         return list(records) or []


# print(DatabaseQueries().select_all('user_name_AND_user_surname', table_name='User_Model'))