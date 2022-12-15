"""
* Assignment: Type Int Mul
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Calculate altitude in meters:
        a. Armstrong Limit: 19 km
        b. Stratosphere: 20 km
        c. USAF Space Line: 80 km
        d. IAF Space Line: 100 km
    2. Run doctests - all must succeed

References:
    * USAF - United States Air Force
    * IAF - International Astronautical Federation
    * Kármán line (100 km) - boundary between Earth's atmosphere and space
    * Armstrong limit (19 km) - altitude above which atmospheric pressure is
      sufficiently low that water boils at the temperature of the human body

Hints:
    * 1 km = 1000 m
    * Use // to get floor division as int

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert armstrong_limit is not Ellipsis, \
    'Assign your result to variable `armstrong_limit`'
    >>> assert stratosphere is not Ellipsis, \
    'Assign your result to variable `stratosphere`'
    >>> assert usaf_space is not Ellipsis, \
    'Assign your result to variable `usaf_space`'
    >>> assert iaf_space is not Ellipsis, \
    'Assign your result to variable `iaf_space`'
    >>> assert type(armstrong_limit) is int, \
    'Variable `armstrong_limit` has invalid type, should be int'
    >>> assert type(stratosphere) is int, \
    'Variable `stratosphere` has invalid type, should be int'
    >>> assert type(usaf_space) is int, \
    'Variable `usaf_space` has invalid type, should be int'
    >>> assert type(iaf_space) is int, \
    'Variable `iaf_space` has invalid type, should be int'

    >>> armstrong_limit
    19000
    >>> stratosphere
    20000
    >>> usaf_space
    80000
    >>> iaf_space
    100000
"""

m = 1
km = 1000 * m

# 19 kilometers in meters
# type: int
armstrong_limit = 19 * km

# 20 kilometers in meters
# type: int
stratosphere = 20 * km

# 80 kilometers in meters
# type: int
usaf_space = 80 * km

# 100 kilometers in meters
# type: int
iaf_space = 100 * km
