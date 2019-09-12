from importlib import import_module
import re
from games.bank.settings.configuration import BASE_DIR

# class SettingsChecker:
#     """
#     This class checks that the values in the
#     configuration file is correctly configured
#     and that the base settings are present
#     """
#     def _check(self):
#         base_settings = ['APPS', 'BASE_DIR', 'DATABASE']
#         settings = self._settings
#         for setting, value in settings.items():
#             if setting not in base_settings:
#                 print('%s was not present in your configuration file. Did you forget to register it?' % setting)

#             if setting == 'APPS':
#                 if not isinstance(value, list):
#                     pass
            
#             if setting == 'BASE_DIR':
#                 if not isinstance(value, str):
#                     pass
            
#             if setting == 'DATABASE':
#                 if not isinstance(value, dict):
#                     pass

class Settings:
    """A wrapper for the configuration file
    """
    def __init__(self):
        # Import the module dynamically
        settings = import_module('configuration')
        # Get the dictionnary
        settings_dict = settings.__dict__

        self.settings = {}
        for setting, value in settings_dict.items():
            if re.search(r'[A-Z]', setting):
                self.settings[setting] = value

    @property
    def settings(self):
        return self.settings
    
    def update_settings(self, setting, value):
        self.settings.update({setting, value})
        return self.settings

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return str(self.settings)

    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

    def __getattribute__(self, name):
        return super().__getattribute__(name)
