"""
* Assignment: Type Float Percent
* Required: no
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. International Standard Atmosphere (ISA) at sea level is
       1 ata = 1013.25 hPa
    2. Calculate `pO2` - partial pressure of Oxygen at sea level in hPa
    3. To calculate partial pressure use ratio
       (100% is 1013.25 hPa, 20.946% is how many hPa?)
    4. Run doctests - all must succeed

Hints:
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert pO2 is not Ellipsis, \
    'Assign your result to variable `pO2`'
    >>> assert type(pO2) is float, \
    'Variable `pO2` has invalid type, should be float'

    >>> ata
    101325.0
    >>> round(pO2, 1)
    212.2
"""

PERCENT = 100
N2 = 78.084 / PERCENT
O2 = 20.946 / PERCENT
Ar = 0.9340 / PERCENT
CO2 = 0.0407 / PERCENT
Others = 0.001 / PERCENT

Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa

# Standard atmosphere (ATA) is pressure at sea level: 1013.25 hectopascals
# type: float
ata = 1013.25 * hPa

# 20.946% of pressure at sea level in hPa, round to one decimal place
# type: float
pO2 = ata * O2 / PERCENT


if __name__ == "__main__":
    import doctest
    doctest.testmod()
