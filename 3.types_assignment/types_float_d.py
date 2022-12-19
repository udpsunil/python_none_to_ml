"""
* Assignment: Type Float Euler
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Euler's number is 2.71828
    2. Round number using f-string formatting
    3. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, \
    'Assign your result to variable `a`'
    >>> assert b is not Ellipsis, \
    'Assign your result to variable `b`'
    >>> assert c is not Ellipsis, \
    'Assign your result to variable `c`'
    >>> assert d is not Ellipsis, \
    'Assign your result to variable `d`'
    >>> assert type(a) is str, \
    'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, \
    'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, \
    'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, \
    'Variable `d` has invalid type, should be str'

    >>> a
    "Euler's number with 0 decimal places: 3"
    >>> b
    "Euler's number with 1 decimal places: 2.7"
    >>> c
    "Euler's number with 2 decimal places: 2.72"
    >>> d
    "Euler's number with 3 decimal places: 2.718"
"""

EULER = 2.71828

# Euler's number with 0 decimal places
# type: str
a = f"Euler's number with 0 decimal places: {EULER:0.0f}"

# Euler's number with 1 decimal places
# type: str
b = f"Euler's number with 1 decimal places: {EULER:0.1f}"

# Euler's number with 2 decimal places
# type: str
c = f"Euler's number with 2 decimal places: {EULER:0.2f}"

# Euler's number with 3 decimal places
# type: str
d = f"Euler's number with 3 decimal places: {EULER:0.3f}"


if __name__ == "__main__":
    import doctest
    doctest.testmod()