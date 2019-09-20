import sqlite3
from games.bank.database.expressions import SQLStatement
from collections import defaultdict

class Query:
    cache = []
    obj_id = None
    columns = ['id', 'name', 'surname']

    def __init__(self, obj, **kwargs):
        # if callable(obj):
        #     # Cache the data in case
        #     # we need to use the obj callable
        #     # later on
        #     obj_cache = obj()
        #     obj = obj_cache

        # if not isinstance(obj, (list, tuple)):
        #     raise TypeError(f'{obj} should be a tupe, list or'\
        #              ' a callable that returns one or the other.')

        # First value should normally be
        # and id of some sort
        # self.obj_id = obj[0]
        self.obj = obj
        # Objectify each items
        self.query = self.mapper()

    def mapper(self):
        # We objectify each returned items
        # so that we can extend them later
        class Item:
            _all = self.obj

            @property
            def _mapped(self):
                return self.__dict__

        for i in range(0, len(self.obj)):
            setattr(Item, self.columns[i], self.obj[i])

        return Item

    # def __setattr__(self, column, value):
    #     print(column)
    #     return super().__setattr__(column, value)

    # def __unicode__(self):
    #     return str(self.cache)

    # def __repr__(self):
    #     return 'Query(%s)' % self.__unicode__()

print(Query([1, 'Kendall', 'Jenner']).query.surname)

class QuerySet:
    """A wrapper class used extend database queries with
    additional functionalities.

    Description
    -----------

    `objs` is a sqlite .cursor() method that wraps
    the results of a query into an object that can be 
    converted for example into a list
    """

    objs_cache = None

    def __init__(self, objs, **kwargs):
        # Cache objects -;
        # When using the objs once,
        # you cannot access them another time
        # self.objs_cache = list(objs).copy()
        # obj is the .cursor() method
        # object returned by an SQL instruction
        # such as SELECT
        # ..
        # Convert obj as list
        queryset = list(objs)
        self.queryset  = queryset

    def __unicode__(self):
        return f'QuerySet({self.queryset})'

    def __repr__(self):
        return self.__unicode__()

    def __getitem__(self, index):
        values = self.queryset[index]
        return str(values)

    def __len__(self):
        return len(self.queryset)

    def count(self):
        return self.__len__()
