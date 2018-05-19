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
        self.mod = mod
        pattern = r'[a-zA-Z]+'
        # e.g. [__attributes__]
        for attr in dir(mod):
            # Get none underscored 
            # attributes e.g. __file__
            if re.search(pattern, attr):
                # Set attributes to class
                attr_value = getattr(mod, attr)
                setattr(self, attr, attr_value)

    def __repr__(self):
        # Returns itself automatically
        # on class call ./. Is callable
        return '<%(cls)s "%(module)s>"' % {
            'cls':self.__class__.__name__,
            'module':self.mod,
        }
