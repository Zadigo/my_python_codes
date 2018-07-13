from importlib import import_module

from test2 import conf_settings
from test2.conf_settings import APPS

# Get each modules in
# the application
# for element in APPS:
#     module_dictionnary = {}
#     try:
#         module = import_module(element)
#     except ImportError:
#         pass
#     else:
#         module_dictionnary[module.__name__] = module


# Get each key in
# the configuration file
# setting_module = conf_settings.__dict__
# SETTINGS = {}

# for key, setting in setting_module.items():
#     if setting is not None:
#         if key.isupper() is True:
#             SETTINGS[key] = setting

# if 'APPS' not in SETTINGS:
#     raise BaseException('APPS could not be found in settings module')


#  The database
# if 'DATABASE' not in SETTINGS:
#     raise BaseException('DATABASE could not be found in settings module')
# else:
#     database = SETTINGS['DATABASE']
#     if not isinstance(database, dict):
#         raise TypeError('DATABASE is not a dict. Received %s' % 
#                         SETTINGS['DATABASE'].__class__.__name__)

# import sqlite3 as db
# class BaseDatabase:
#     def __init__(self):
#         keys = ['user', 'password']
#         for key, attribute in database.items():
#             if key in keys:
#                 setattr(BaseDatabase, key, attribute)

# class Database(BaseDatabase):
#     def show(self):
#         print(self.user)




# Metaclasses
# class Base(type):
#     def __new__(self,  clsname, bases, clsdict):
#         new_class = super().__new__(self,  clsname, bases, clsdict)
#         setattr(new_class, 'test', 'test')
#         return new_class

# class Subbase(metaclass=Base):
#     pass

# class TestBase(Subbase):
#     pass


# Decorate class
# def decorate1(*args, **kwargs):
#     def _dec(instance):
#         if kwargs:
#             # Get the model
#             if 'model' in kwargs:
#                 model = kwargs['model']
#             if isinstance(instance, model):
#                 for key, value in kwargs.items():
#                     if key != 'model':
#                         setattr(model, key, value)
#         return model
#     return _dec

# class W:
#     def a(self):
#         print('a')

# i = W()
# a = decorate1(value='value', model=W)
# z = a(i)
# z().a()


# Decorate class
def decorate2(model):
    def _dec(*args):
        model_dict = model.__dict__
        print(model_dict)
    return _dec

class B:
    pass

@decorate2
class A:
    def test(self):
        pass

a = A('test', 'value')
