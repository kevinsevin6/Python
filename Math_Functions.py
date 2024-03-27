# Rounding function
x = 2.9
print(round(x))
x = 2.5         # rounded down to 2 ??
print(round(x))
x = 2.4         # rounded down to 2
print(round(x))
x = 2.6         # rounded up to 3
print(round(x))
# so it seems that it splits between 5 and 6 instead of 4 and 5

# Absolute function
print(abs(-2.9))

# Importing the math module
import math
# typing math. will show you all the functions available in this module
print(math.ceil(2.9))
print(math.floor(2.9))
# you can just google python 3 math module and check out the docs for the list of all functions in this module
