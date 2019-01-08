import spread_settings
from importlib import import_module
import os
import re

class GlobalSettings:
    def __init__(self):
        for setting in dir(spread_settings):
            if setting.upper():
                setattr(self, setting, getattr(spread_settings, setting))

        if not os.path.exists(self.JSON_KEY_FILE):
            print('No secret')

        settings_with_tuples = [
            'SHEETS',
            'SHEET_RANGES'
        ]

        if not self.SPREADSHEET:
            print('You need to specify a spreadsheet')

        if not self.SHEET:
            print('You need to specify a sheet name')
        else:
            if not isinstance(self.SHEET, str):
                print('The sheet name must be a string value')

        if not self.SHEET_RANGE:
            print('No range was specified')
        else:
            if not isinstance(self.SHEET_RANGE, str):
                print('Sheet range to work with must be a string')

        # if self.SHEETS:
        #     if not isinstance(self.SHEETS, (tuple, list)):
        #         print('Sheets should be a tuple or a list')

        # if self.SHEET_RANGES:
        #     if not isinstance(self.SHEET_RANGES, (tuple, list)):
        #         print('Sheet ranges should be a tuple or a list')

    def __repr__(self):
        return '<%(cls)s "%(settings_module)s">' % {
            'cls': self.__class__.__name__,
            'settings_module': self
        }


class LazySettings:
    def _setup(self, name=None):
        self.wrapped_settings = GlobalSettings()
        print(self.wrapped_settings)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
