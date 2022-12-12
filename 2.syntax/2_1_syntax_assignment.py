"""
- identifier is a formal name for variable
- variables can change its value during the program
- there are no constants in python, only naming convention to indicate constant as a convention
- 'NameError' when using a undeclared variable
- 'AttributeError' when a variable can not be assigned
"""

# Variables

# identifier are case sensitive
name = 'Sunil Udupi'

# underscore is used for multi-word names
first_name = 'Sunil'
last_name = 'Udupi'

# variables names can be joined without _
firstname = 'Sunil'
lastname = 'Udupi'

# Camel Case is not used in Python by convention
#   firstName
# Pascal Case is reserved for Class Names
#   Firstname or FirstName

# numbers can be used in variable names but they can't appear first
name1 = 'Sunil'
# 1name


# Constants
# By convention variable names with all capitals are considered as constants
FILE = '/etc/passwd'
FILENAME = '/etc/group'
FILE_NAME = '/etc/shadow'

# Conventions
name = 'Sunil Udupi'    # variable
NAME = 'SUNIL UDUPI'    # constant
Name = 'Sunil Udupi'    # class

# Examples of Constants by convention
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

workday = 8 * HOUR
workweek = 40 * HOUR

# Example where Constants convention doesn't make sense.
Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
MPa = 1000000 * Pa

# Declaring above constants in all caps won't help readability


## Types
# Basic Types
data = 1        # int
data = 1.2      # float
data = True     # bool
data = None     # NoneType
data = 'abc'    # str

# Sequences
data = [1, 2, 3,]           # list
data = (1, 2, 3)            # tuple
data = {1, 2, 3}            # set
data = {'a':1, 'b':2, "c":3}# dict