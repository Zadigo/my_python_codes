import sqlite3
from sqlite3.test import transactions
import re

import os
PATH='C:\\Users\\Pende\\Documents\\Python\\specialrequests\\sr_database'

class BaseDatabase:
    def __init__(self, alternate_db=''):
        if alternate_db:
            is_correct = re.match(r'\w+\.sqlite', alternate_db)
            if not is_correct:
                raise TypeError("Votre base de données ne respecte pas \
                     le format 'nom.sqlite': %s" % alternate_db)
            self.database = sqlite3.connect(os.path.join(PATH, alternate_db))
        else:
            self.database = sqlite3.connect('data.sqlite')
        self.cursor = self.database.cursor()

    def __repr__(self):
        return "<class '%(cursor)s'>" % {
            'cursor': self.cursor
        }

class QuerySelectors(BaseDatabase):
    def _auto_migrate(self):
        sql = "CREATE TABLE responses (response_id INTEGER PRIMARY KEY, response_name CHAR(100))"
        print("Creating tables...")
        self.cursor.execute(sql)
        self.database.commit()
        self.database.close()
        

    def get(self, **kwargs):
        methods = ['exact', 'contains']
        for accessor, value in kwargs.items():
            field, method = accessor.split('__')

            if method == 'exact':
                evaluation = "%s LIKE '%s'" % (field, value)
                
            
        #     if method == 'contains':
        #         evaluation = "%s LIKE '*%s*'" % (field, value)

            sql = "SELECT * FROM %(database)s WHERE %(evaluation)s" % {
                'database': 'test',
                'evaluation': evaluation
            }

    def _put(self, **kwargs):
        columns=((column) for column, value in kwargs.items())
        values=((value) for column, value in kwargs.items())
        
        sql = "INSERT INTO %(database)s%(columns)s VALUES%(values)s" % {
            'database': 'test',
            'columns': tuple(columns),
            'values': tuple(values)
        }
        print(sql)


QuerySelectors()._put(co_o='part',that='that')

# a="SELECT %(fields)s FROM %(database)s" % {''
#     'fields': ', '.join(['a','b']),
#     'database':'test'
# }

# evaluation='test__iexact'
# field, s = evaluation.split('__')
# if s == 'iexact':
#     t='%s LIKE %s' % (field, "'a'")
# c="SELECT %(fields)s FROM %(database)s WHERE %(evaluation)s" % {''
#     'fields': ', '.join(['a','b']),
#     'database':'test',
#     'evaluation': t
# }


# def test(**kwargs):
#     print(kwargs)

# test(at__i='ttt')