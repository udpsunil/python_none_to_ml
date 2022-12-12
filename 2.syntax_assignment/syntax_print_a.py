"""
* Assignment: Syntax Print Newline
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result` with text 'Hello World'
    2. 'Hello' must be in a first line
    3. 'World' must be in a second line
    4. Run doctests - all must succeed

Hints:
    * Either quotes (") or apostrophes (') will work

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert 'Hello' in result, \
    'Word `Hello` must be in the `result`'
    >>> assert '\\n' in result, \
    'Newline `\\n` must be in the `result`'
    >>> assert 'World' in result, \
    'Word `World` must be in the `result`'
"""

# with Hello and World in separate lines
# type: str
result = 'Hello\nWorld'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
