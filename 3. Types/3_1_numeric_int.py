# Numeric Int
'''
- Represents signed & unsigned integer.
- Default size is 64bit and there is no maximum or minimum value
- Python automatically extends int when bigger number is needed
'''

import string
data = 1
data = +1
data = -1

# _ can be used to separate digits
million = 1000000
million = 1_000_000
print(million)

# Type casting
'''
int() converts arguments to int
works with strings if a character can be converted to int
supports +, - & _
'''

data = 'abc'
try:
    int(data, base=10)
except ValueError:
    print("Invalid base used for conversion")

print(int(data, base=16))

print(string.hexdigits)
print(string.octdigits)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

x = 1
print(type(x))
print(type(x) is int)
print(isinstance(x, int))

'''
using int() to round a floating value doesn't produce required rounding effect. 
use round() for numbers rounding
'''

'''
built-in functions
abs() - absolute value
pow() - raise number to power of exponential
'''
print(abs(1) == abs(-1))
print(pow(2, 4))
print(pow(16, 1/2))

# use case 0x01
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

duration = 123456 * SECOND
print(duration // DAY)
print(duration // HOUR)
print(duration // MINUTE)
print(duration // SECOND)

# use case 0x02
m = 1
km = 1000 * m
mi = 1652 * m

distance = 123 * mi
print(distance // m)
print(distance // km)

# use case 0x03
PLN = 1
EUR = 4.63 * PLN
USD = 4.20 * PLN

cena = 100 * PLN
print(round(cena // EUR))
print(round(cena // USD))
