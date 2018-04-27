import re
# import sqlite3 as db
# import os

# # DATABASE_PATH = os.path.join(os.getcwd(), 'Python\\python_codes\\Banque\\bank_db.db')
# DATABASE_PATH = 'bank.db'

# class DataBaseMixins:
#     context = None
    
#     def get_context(self, *args, **kwargs):
#         # Puts context
#         if self.context is not None:
#             kwargs.update(context=self.context)

#         # Puts instance of class
#         if 'method' not in kwargs:
#             kwargs['method'] = self

#         return kwargs


# class DataBase(DataBaseMixins):
#         def _cursor(self):
#             try:
#                 # Connect to database, 
#                 _conn = db.connect(DATABASE_PATH)

#             except Exception as error:
#                 print('There was an error. %s' % error.args )
#                 raise
            
#             with _conn:
#                 self._cursor = _conn.cursor()
#                 return self._cursor


# class DatabaseQueries(DataBase):
#     table_name = None

#     def select_user(self, **kwargs):
#         SQL = 'SELECT * FROM User_Model WHERE user_name=?'
#         records = super()._cursor().execute(SQL, (kwargs.get('username'),))
#         return list(records) or []

#     def select_all(self, *args, **kwargs):
#         if 'table_name' in kwargs:
#             self.table_name = kwargs.get('table_name')

#         SQL = 'SELECT * FROM ' + self.table_name

#         records = super()._cursor().execute(SQL)
#         return list(records) or []


# print(DatabaseQueries().select_all('user_name_AND_user_surname', table_name='User_Model'))


SQL_COMMANDS = [
    r'^([a-zA-Z\_]+)(AND)([\_a-zA-Z]+)',
    r'^([a-zA-Z\_]+)(AND)([\_a-zA-Z]+)(AND)([\_a-zA-Z]+)',
]

a=re.search(SQL_COMMANDS[0], 'user_name_AND_user_surname')
p=a.group()
p=a.group()
p=a.group()