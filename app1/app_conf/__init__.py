import app_global_settings
import importlib

class Settings:
    def __init__(self, settings_module):
        # Get elements in module
        for setting in dir(app_global_settings):
            if setting.isupper():
                setattr(self, setting, getattr(app_global_settings, setting))
        self.SETTINGS_MODULE=settings_module

        mod = importlib.import_module(self.SETTINGS_MODULE)

        tuple_settings = (
            "INSTALLED_APPS",
            "TEMPLATE_DIRS",
            "LOCALE_PATHS",
        )
        self._explicit_settings = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)

                # if setting in tuple_settings and not isinstance(setting_value, (tuple, list)):
                #     raise ValueError

                setattr(self, setting, setting_value)

    def __repr__(self):
        return '<%(cls)s "%(settings_module)s">' % {
            'cls': self.__class__.__name__,
            'settings_module': self.SETTINGS_MODULE,
        }

Settings('app_global_settings').__repr__()