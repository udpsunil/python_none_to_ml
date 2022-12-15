"""
* Assignment: Type Int Bits
* Required: no
* Complexity: medium
* Lines of code: 4 lines
* Time: 3 min

English:
    1. File size is 1337 megabits [Mb]
    2. Calculate size in bits [b]
    3. Calculate size in kilobits [kb]
    4. In Calculations use floordiv (`//`)
    5. Run doctests - all must succeed

Hints:
    * 1 kb = 1024 b
    * 1 Mb = 1024 Kb
    * Use // to get floor division as int

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert size_b is not Ellipsis, \
    'Assign your result to variable `size_b`'
    >>> assert size_kb is not Ellipsis, \
    'Assign your result to variable `size_kb`'
    >>> assert size_Mb is not Ellipsis, \
    'Assign your result to variable `size_Mb`'
    >>> assert type(size_b) is int, \
    'Variable `size_b` has invalid type, should be int'
    >>> assert type(size_kb) is int, \
    'Variable `size_kb` has invalid type, should be int'
    >>> assert type(size_Mb) is int, \
    'Variable `size_Mb` has invalid type, should be int'

    >>> size_b
    1401946112
    >>> size_kb
    1369088
    >>> size_Mb
    1337
"""

b = 1
kb = 1024 * b
Mb = 1024 * kb

SIZE = 1337 * Mb

# SIZE in bits
# type: int
size_b = SIZE

# SIZE in kilobits
# type: int
size_kb = SIZE // kb

# SIZE in megabits
# type: int
size_Mb = SIZE // Mb
