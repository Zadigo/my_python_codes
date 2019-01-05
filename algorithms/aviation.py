from dataclasses import dataclass
from collections import namedtuple
import datetime
import statistics
import math

def millibar_to_pascal(self, value):
    return value * 100

class Heights(object):
    def __new__(cls):
        self = object.__new__(cls)
        self._millibar = 0.038640888
        return self
    
    def qnh_to_qfe(self, airfield_elevation):
        millibar_in_feet = 0.038640888
        r = airfield_elevation / (millibar_in_feet * 100)
        qfe = 1023
        print(r+qfe)

    def __repr__(self):
        """
        Convert to formal string, for repr().

        >>> dt = datetime(2010, 1, 1)
        >>> repr(dt)
        'datetime.datetime(2010, 1, 1, 0, 0)'
        """
        t=namedtuple('Heights', ['a'])
        return '%s(%s, %s)' % (
            self.__class__.__qualname__,
            self._millibar,
            t(15)
        )
