"""
* Assignment: Syntax Variables Int
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with value 1
    2. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is int, \
    'Variable `result` has invalid type, should be int'
    >>> assert result == 1, \
    'Variable `result` has invalid value, should be 1'
"""
result: int = 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
