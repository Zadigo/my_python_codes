import sqlite3

import psycopg2

from model_fields import CharField, IntegerField

# from django.db.models.fields import CharField
        



class Options:
    def __init__(self):
        self.db = 'test'
        self.db_table = ''

class BaseModel(type):
    def __new__(cls, cls_name, bases, cls_dict):
        super_new = super().__new__
        new_class = super_new(cls, cls_name, bases, cls_dict)
        new_class.add_to_class('_meta', Options())

        # On récupère les sous-classes
        parents = [b for b in bases if issubclass(Model, b)]

        # On récupère tous les attributs des
        # sous-classes
        for field_name, field_value in cls_dict.items():
            new_class.add_to_class(field_name, field_value)
        
        return new_class

    def add_to_class(cls, name, value):
        setattr(cls, name, value)

class Model(metaclass=BaseModel):
    def __init__(self, *args, **kwargs):
        pass

class TestTable(Model):
    nom = CharField(max_length=255)


print(TestTable()._meta.db)
