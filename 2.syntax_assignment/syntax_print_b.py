"""
* Assignment: Syntax Print Interpolation
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result` with text 'Hello NAME'
    2. Insted `NAME` substitute "Mark Watney"
    3. To substitute use f-string notation and `{variable}`
    4. Run doctests - all must succeed

Hints:
    * Either quotes (") or apostrophes (') will work
    * Use f-string

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert 'Mark Watney' in result, \
    'Variable `result` does not contain string "Mark Watney"'
    >>> assert '{NAME}' not in result, \
    'You must use f-string'

    >>> result
    'Hello Mark Watney'
"""

NAME = 'Mark Watney'

# Define result with text: `Hello NAME`
# Variable NAME should be interpolated
# type: str
result = f'Hello {NAME}'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
