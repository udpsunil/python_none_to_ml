"""
>>> import sys
>>> sys.tracebacklimit = 0
>>> assert sys.version_info > (3, 8, 0), 'python 3.8 is required'
>>> assert python_executable
>>> assert python_version
"""
import os
import sys

print(f"Your python version is {sys.version[:6]}")
python_executable = sys.executable
python_version = tuple(sys.version_info)
venv = os.getenv("VIRTUAL_ENV")
print(python_executable)
print(python_version)
print(venv)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
