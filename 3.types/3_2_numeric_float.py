"""
- represents both signed and unsigned float with a size of 64 bit.
- automatically extends float when a bigger type is needed
"""

import math


data = 1.337
data = +1.337
data = -1.337

# with/without zero notation
data = 0.44
data = .44
data = 44.
data = 44.0

# engineering notation
x = 1e6
print(x)
x = 1E6
print(x)
x = +1e6
print(x)
x = -1e6
print(x)
x = 1e-3
print(x)

# type casting
float(1)
float(+1)
float(-1)
pi = math.pi
print(pi)
print(round(pi, 4))
print(f'Pi is {pi:f}')
print(f'Pi is {pi:.4f}')
print(f'Pi is {pi:.2f}')
print(f'Pi is {pi:.0f}')
