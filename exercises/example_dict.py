import importlib
from collections import 

module = importlib.import_module('toupa')

class A():
    def __init__(self):
        self.__dict__['sample_dict'] = set()
        self.custom_attrib = module

    def __getattr__(self, name):
        return getattr(self.custom_attrib, name)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def __delattr__(self, name):
        super().__delattr__(name)

    def __dir__(self):
        pass

    def __repr__(self):
        return '<%(cls)s>' % {
            'cls': self.__class__.__name__,
        }