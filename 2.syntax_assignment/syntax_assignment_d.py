"""
* Assignment: Syntax Variables Bool
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with value True
    2. Run doctests - all must succeed

Hint:
    * Note that True is capitalized

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is bool, \
    'Variable `result` has invalid type, should be bool'
    >>> assert result is True, \
    'Variable `result` has invalid value, should be True'
"""

# with value True
# type: bool
result = True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
