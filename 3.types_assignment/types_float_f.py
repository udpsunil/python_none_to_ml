"""
* Assignment: Type Float Pressure
* Required: no
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Operational pressure of EMU spacesuit: 4.3 PSI
    2. Operational pressure of ORLAN spacesuit: 40 kPa
    3. Calculate operational pressure in hPa for EMU
    4. Calculate operational pressure in hPa for Orlan
    5. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert emu is not Ellipsis, \
    'Assign your result to variable `emu`'
    >>> assert orlan is not Ellipsis, \
    'Assign your result to variable `orlan`'
    >>> assert type(emu) is float, \
    'Variable `emu` has invalid type, should be float'
    >>> assert type(orlan) is float, \
    'Variable `orlan` has invalid type, should be float'

    >>> round(orlan, 1)
    400.0
    >>> round(emu, 1)
    296.5
"""

Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
psi = 6894.757 * Pa

# 4.3 pounds per square inch in hectopascals, round to one decimal place
# type: float
emu = 4.3 * psi / hPa

# 40 kilopascals in hectopascals, round to one decimal place
# type: float
orlan = 40 * kPa / hPa

if __name__ == "__main__":
    import doctest
    doctest.testmod()
