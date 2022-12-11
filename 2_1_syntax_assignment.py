"""
- identifier is a formal name for variable
- variables can change its value during the program
- there are no constants in python, only naming convention to indicate constant as a convention
- 'NameError' when using a undeclared variable
- 'AttributeError' when a variable can not be assigned
"""

## Variables

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


## Constants
# By convention variable names with all capitals are considered as constants
FILE = '/etc/passwd'
FILENAME = '/etc/group'
FILE_NAME = '/etc/shadow'

# Conventions
name = 'Sunil Udupi'    # variable
NAME = 'SUNIL UDUPI'    # constant
Name = 'Sunil Udupi'    # class