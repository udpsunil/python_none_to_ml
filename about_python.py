"""
>>> sys.tracebacklimit = 0
>>> assert sys.version_info > (3, 8, 0), 'python 3.8 is required'
"""
import sys

print(f"Your python version is {sys.version[:6]}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
