from base import Bank
from base1 import Database



# import hash_helper as hs
# import sqlite3 as db
# import os

# FILE_LOCATION = 'D:\\Programs\\Python\\Banque\\bank_db.db'
# USER = {
#     'name': 'Juline',
#     'surname': 'Matthieur',
#     'user_hash': 'fdsnf4564sdfsfsdfdf',
#     'account': 1,
#     'created_at': '18/03/2018',
#     'updated_at': '18/03/2018'
# }

# class Bank(object):
#     def __init__(self):
#         self.conn = db.connect(FILE_LOCATION)
#         with self.conn:
#             self._cursor = self.conn.cursor()
        
# class Orders(Bank):
#     def _select_data(self):
#         sql = 'SELECT name, surname FROM Users WHERE user_hash_key = ?'
#         return self._cursor.execute(sql, (USER['user_hash'],))
    
#     def _insert_data(self, sql=''):
#         if sql == '':
#             sql = 'INSERT INTO Users VALUES(?, ?, ?, ?, ?, ?)'
#         self._cursor.execute(sql, (USER['name'], USER['surname'], USER['user_hash'], USER['account'], USER['created_at'], USER['updated_at']))
#         self.conn.commit()
    
#     def _update_data(self, sql=''):
#         if sql=='':
#             sql = 'UPDATE Users SET ? WHERE  ? = ?'
#             self._cursor.execute(sql, ())
        

# # Orders()._insert_data('')
# a = Orders()._select_data()
# for t in a:
#     print(t)