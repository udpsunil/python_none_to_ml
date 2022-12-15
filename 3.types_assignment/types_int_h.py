"""
* Assignment: Type Int Bandwidth
* Required: no
* Complexity: easy
* Lines of code: 10 lines
* Time: 3 min

English:
    1. Having internet connection with speed 100 Mb/s
    2. How long will take to download 100 MB?
    3. To calculate time divide file size by speed
    4. Note, that all values must be `int` (type cast if needed)
    5. In Calculations use floordiv (`//`)
    6. Run doctests - all must succeed

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB
    * Use // to get floor division as int

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert bandwidth is not Ellipsis, \
    'Assign your result to variable `bandwidth`'
    >>> assert size is not Ellipsis, \
    'Assign your result to variable `size`'
    >>> assert duration is not Ellipsis, \
    'Assign your result to variable `duration`'
    >>> assert type(bandwidth) is int, \
    'Variable `bandwidth` has invalid type, should be int'
    >>> assert type(size) is int, \
    'Variable `size` has invalid type, should be int'
    >>> assert type(duration) is int, \
    'Variable `duration` has invalid type, should be int'

    >>> duration
    8
"""

SECOND = 1

b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

# 100 megabits per second
# type: int
bandwidth = 100 * Mb

# 100 megabytes
# type: int
size = 100 * MB

# Duration is size by bandwidth in seconds
# type: int
duration = size // bandwidth
