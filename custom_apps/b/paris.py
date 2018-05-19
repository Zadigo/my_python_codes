import os
import re
import importlib

dotted_path = 'b.toupa'
module_path, module = dotted_path.rsplit('.', 1)

class A:
    """
    Example of an application that imports
    another module and sets its attributes
    to a class
    """
    def __init__(self):
        # Import module
        mod = importlib.import_module(module)
        # e.g. [__attributes__]
        attrs = dir(mod)
        for attr in attrs:
            that = re.search(r'[a-zA-Z]+', attr)
            if that:
                # Set attributes to class
                setattr(self, attr, getattr(mod, attr))

    def __repr__(self):
        # Returns itself automatically
        # on class call
        return '<%(cls)s: "%(class)s>"' % {
            'cls':self.__class__.__name__,
            'class':self.__class__,
        }

class T(A):
    def show(self):
        a = super(T, self)
        print(a)

p=T()
p.show()