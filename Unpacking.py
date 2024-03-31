coordinates = (1, 2, 3)
result = coordinates[0] * coordinates[2] * coordinates[1]
print(result)
# can get messy and complicated

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

result = x * y * z
print(result)
# much better, but there is an easier way of doing this

x, y, z = coordinates                   # unpacking
print(x)
print(y)
print(z)

list = ['kebin', 'sebin', 'six']        # works with lists too
a, b, c = list
print(a)
print(b)
print(c)

#a, b, c, d, e = list                    # Error: not enough values to unpack
#a, b = list                             # Error: too many values to unpack

# So the number of variables and items in the list must equal
