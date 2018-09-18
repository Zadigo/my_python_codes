import importlib

class A:
    def __init__(self):
        a = importlib.import_module('test1')
        p = a.__dict__
        for item, func in p.items():
            if callable(func):
                print(func)

A()