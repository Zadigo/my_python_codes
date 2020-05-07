# from dataclasses import dataclass
# from collections import namedtuple
# import datetime
# import statistics
# import math

# def millibar_to_pascal(self, value):
#     return value * 100

# class Heights(object):
#     def __new__(cls):
#         self = object.__new__(cls)
#         self._millibar = 0.038640888
#         return self
    
#     def qnh_to_qfe(self, airfield_elevation):
#         millibar_in_feet = 0.038640888
#         r = airfield_elevation / (millibar_in_feet * 100)
#         qfe = 1023
#         print(r+qfe)

#     def __repr__(self):
#         """
#         Convert to formal string, for repr().

#         >>> dt = datetime(2010, 1, 1)
#         >>> repr(dt)
#         'datetime.datetime(2010, 1, 1, 0, 0)'
#         """
#         t=namedtuple('Heights', ['a'])
#         return '%s(%s, %s)' % (
#             self.__class__.__qualname__,
#             self._millibar,
#             t(15)
#         )



import datetime
from collections import namedtuple

def calculate_time(distance, speed):
    """Calculate the time required to get from
    a point A to a point B
    
    Parameters
    ----------
    
        distance: nautical miles

        speed: knots

    Example
    -------

    >>> calculate_time(400, 315)
    >>> 1.27 hours
    """
    value = namedtuple('CalculatedTime', ['time'])
    return value(round(distance / speed, 3))

def calculate_distance(speed, _time):
    """Calculate the distance required to get from
    a point A to a point B
    
    Parameters
    ----------
    
        speed: knots

        time: hours

    Example
    -------

    >>> calculate_time(310, 1.54)
    >>> 477.4 nautical miles
    """
    value = namedtuple('CalculatedDistance', ['distance'])
    return value(round(speed * _time, 3))

def descent_rate(start, end, distance, speed, adjust_degree_by=0, round_to=0):
    """Calculate the descent rate from a point
    A to a point B

    Parameters
    ----------

        start // end: foot

        distance: nautical miles

        speed: knots

        round_to: Adds extra feet in order to not be too high

    Description
    -----------

        FTD: The remaining amount of feet to descend (feet)

        DNM: The amount of feet descended by nautical miles (miles)

        MPM: Amount of miles travelled per minute (miles per minute)

        DR: Descent rate (feet)

        ADR: Adjusted descent rate (feet)

    Example
    -------

        descent_rate(7100, 6700, 4, 120)

        DescentRate(FTD=400, DNM=100.0, MPM=1.67, DR=167.0)

    """
    # https://www.boldmethod.com/learn-to-fly/navigation/how-to-calculate-your-required-descent-rate-to-mda/

    feet_to_descend = start - end
    descent_per_nm = feet_to_descend / distance
    miles_per_minute = round(descent_per_nm / 60, 2)
    descent_rate = round(1 * miles_per_minute * 100, 0) + round_to

    fields = ['FTD', 'DNM', 'MPM', 'DR']
    if adjust_degree_by > 0:
        fields.append('ADR')
        value = namedtuple('DescentRate', fields)
        adjusted_descent_rate = adjust_degree_by * miles_per_minute * 100 + round_to
        return value(feet_to_descend, descent_per_nm, miles_per_minute, descent_rate, adjusted_descent_rate)

    value = namedtuple('DescentRate', fields)
    return value(feet_to_descend, descent_per_nm, miles_per_minute, descent_rate)

print(descent_rate(7100, 6700, 4, 120, 3, round_to=50))
