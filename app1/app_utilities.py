import copy
import os
from importlib import import_module
from importlib.util import find_spec as importlib_find

def import_string(dotted_path):
    """
    Use this module to import a class or def from
    a dotted path
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as error:
        raise ImportError('%s is not a module path. %s' % (dotted_path, error.__context__))

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as error:
        raise ImportError('Module "%s" does not contain "%s" as an attribute/class' % (
                module_path, class_name
            )
        )

