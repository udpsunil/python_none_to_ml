# String
# strings work with both " & '

name = 'Sunil Udupi'
name = "Sunil Udupi"

# Syntax Error: unterminated string literal
# name = "Sunil Udupi'
# name = 'Sunil Udupi"

# String interpolation
# f-strings
# str.format()
# %-string is from legacy python 1 and 2

name = 'Sunil Udupi'
result = f'Hello, {name}'
print(result)

result = 'Hello, {0}'.format(name)
print(result)

result = 'Hello, %s' %name
print(result)