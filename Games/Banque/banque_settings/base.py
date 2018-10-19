from importlib import import_module
import re


class Settings:
    def __init__(self):
        settings = import_module('configuration')
        settings_dict = settings.__dict__
        self._settings = {}
        for setting, value in settings_dict.items():
            if re.search(r'[A-Z]', setting):
                self._settings [setting] = value

    @property
    def get_settings(self):
        self._settings
    
    def update_settings(self, setting, value):
        settings = self._settings
        if setting in settings:
            settings[setting] = value
        return settings

class SettingsChecker(Settings):
    """
    This class checks that the values in the
    configuration file is correctly configured
    and that the base settings are present
    """
    def _check(self):
        base_settings = ['APPS', 'BASE_DIR', 'DATABASE']
        settings = self._settings
        for setting, value in settings.items():
            if setting not in base_settings:
                print('%s was not present in your configuration file. Did you forget to register it?' % setting)

            if setting == 'APPS':
                if not isinstance(value, list):
                    pass
            
            if setting == 'BASE_DIR':
                if not isinstance(value, str):
                    pass
            
            if setting == 'DATABASE':
                if not isinstance(value, dict):
                    pass