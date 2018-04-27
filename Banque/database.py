import sqlite3 as db
import os

DATABASE_PATH = os.path.join(os.getcwd(), 'Python\\Banque\\bank_db.db')

class DataBaseMixins:
    context = None
    
    def get_context(self, *args, **kwargs):
        if self.context is not None:
            kwargs.update(context=self.context)

        if 'method' not in kwargs:
            kwargs['method'] = self
            
        return kwargs

print(DataBaseMixins().get_context(context=''))


# class DataBase(DataBaseMixins):
#     timeout = None

#     def __init__(self):
#         if type(timeout).__name__ != 'int':
#             raise TypeError('Value should be an integer. Got %s' % timeout)

#         # Connect to database
#         try:
#             _conn = db.connect(DATABASE_PATH, timeout)

#         except Exception as error:
#             print('There was an error. %s' % error.args )
#             raise
        
#         with _conn:
#             self._cursor = _conn.cursor()
#             return self._cursor


# class Queries(DataBase):
#     table_name = None

#     def select_all(self, *args, **kwargs):
#         if 'table_name' in kwargs:
#             self.table_name = kwargs.get('table')

#         self._cursor.execute('SELECT ? FROM ?', (args, self.table_name,))

    # def select(self, *args, **kwargs):
    #     SQL = 'SE'

    # def insert(self, *args, **kwargs):
    #     pass

    # def delete(self, *args, **kwargs):
    #     pass
