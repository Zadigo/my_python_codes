import os
from importlib import import_module

class AppConfig:
    """
    Class representing an application
    and its configuration within the package
    """

    def __init__(self, app_name, app_module):
        # e.g. 'django.contrib.admin'
        self.name = app_name

        # e.g. <module 'django.contrib.admin'
        # from 'django/contrib/admin/__init__.py'>
        self.module = app_module

        # Reference to the Apps registry that holds this AppConfig. Set by the
        # registry when it registers the AppConfig instance.
        self.apps = None

        # e.g. 'admin'.
        # This value must be unique
        if not hasattr(self, 'label'):
            self.label = app_name.rpartition(".")[2]

        # Human-readable name for the application e.g. "Admin".
        if not hasattr(self, 'verbose_name'):
            self.verbose_name = self.label.title()

        # e.g. '/path/to/django/contrib/admin'.
        if not hasattr(self, 'path'):
            self.path = self._path_from_module(app_module)

        # e.g. <module 'django.contrib.admin.models'
        # from 'django/contrib/admin/models.py'>.
        self.models_module = None
        
        # Mapping of lower case model names to model classes. Initially set to
        # None to prevent accidental access before import_models() runs.
        self.models = None

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.label)

    def _path_from_module(self, module):
        paths = list(getattr(module, '__path__', []))
        filename = getattr(module, '__file__', None)
        paths = [os.path.dirname(filename)]
        return paths[0]

AppConfig('app1.test1.test2', '__init__')
        

        