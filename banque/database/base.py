# import sqlite3 as db
# from collections import OrderedDict

# class BaseDatabase(type):
#     def __new__(cls, clsname, bases, clsdict):
#         try:
#             # Create database instance
#             conn = db.connect('xxxx.db')
#             cursor = conn.cursor()
#         except db.DatabaseError as error:
#             print('Could not connect to database %s' %
#                 error.args
#             )
#             raise
#         else:
#             clsdict['cursor_object'] = cursor
#         new_class = super().__new__(cls, clsname, bases, clsdict)
#         return new_class

# class Database(metaclass=BaseDatabase):
#     pass

# class BaseManager(Database):
#     def get_object(self, sql, *args):
#         return self.cursor_object.execute(sql, ('a',))

# class A(BaseManager):
#     pass

# class B(BaseManager):
#     pass

import re
a = 'a_get_user_1_and_5_or_7'
re.search(r'[and\_\w+]+\_[or\_\w+]+', a)
tablename, command, what, num = a.rsplit('_')
if command == 'get':
    u = 'SELECT %(tablename)s FROM %(what)s' % {
        'tablename': tablename,
        'what': what,
    }

u += ' WHERE %(args)s = %(value)s' % {
    'args': 'po',
    'value': 1,
}
print(u)