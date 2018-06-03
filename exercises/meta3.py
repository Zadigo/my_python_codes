from importlib import import_module
import os

path = 'decorators'
cpath = 'a.b.decorators'

laposter = import_module(path)
path = getattr(laposter, '__file__')
name = getattr(laposter, '__name__')
dirname = os.path.dirname(path)

a, _, c =cpath.rpartition('.')
print(_)