import copy
import os
from importlib import import_module
from importlib.util import find_spec

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
        # Returns function/class within the module
        print(getattr(module, class_name))
        # return getattr(module, class_name)
    except AttributeError as error:
        raise ImportError('Module "%s" does not contain "%s" as an attribute/class' % (
                module_path, class_name
            )
        )

import_string('test_1.google')

def module_has_submodule(package, module_name):
    # From import_module
    # e.g. <module '__name__' from '__path__'>
    package_name = package.__name__
    package_path = package.__path__
    full_module_name = package_name + '.' + module_name
    # Returns the specs of the module
    # e.g. ModuleSpec(name='', loader='', origin='__path__')
    try:
        print(find_spec(full_module_name, package_path))
    except (ImportError, AttributeError):
        return False

def module_dir(module):
    paths = list(getattr(module, '__path__', []))
    filename = getattr(module, '__file__', None)
    print(os.path.dirname(filename))
    raise ValueError('Cannot determine directory containing %s' % module)

# module_has_submodule(import_module('test_1'),'test_1')
# module_dir(import_module('test_1'))