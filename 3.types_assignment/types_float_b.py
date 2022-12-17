"""
* Assignment: Type Float Altitude
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Plane altitude is 10.000 ft
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Result round to one decimal place
    5. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert altitude is not Ellipsis, \
    'Assign your result to variable `altitude`'
    >>> assert altitude_m is not Ellipsis, \
    'Assign your result to variable `altitude_m`'
    >>> assert altitude_ft is not Ellipsis, \
    'Assign your result to variable `altitude_ft`'
    >>> assert type(altitude) is float, \
    'Variable `altitude` has invalid type, should be float'
    >>> assert type(altitude_m) is float, \
    'Variable `altitude_m` has invalid type, should be float'
    >>> assert type(altitude_ft) is float, \
    'Variable `altitude_ft` has invalid type, should be float'

    >>> altitude
    3048.0
    >>> altitude_m
    3048.0
    >>> altitude_ft
    10000.0
"""

m = 1
ft = 0.3048 * m

# 10_000 ft
# type: float
altitude = 10_000 * ft

# Altitude in meters
# type: float
altitude_m = altitude

# Altitude in feet
# type: float
altitude_ft = altitude_m / ft

if __name__ == "__main__":
    import doctest
    doctest.testmod()
