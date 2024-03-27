for item in 'Python':
    print(item)

for item in ['Kebin', 'Debin', 'Eban']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(10):       # for when too many numbers to explicitly write out
    print(item)              # range() does not create a list, but an object. In each iteration the object spits out a different number

for item in range(5, 10):    # starting with 5, to 10 characters
    print(item)

for item in range(5, 10, 2):   # from 5 to 10 in increments of 2
    print(item)


# Ex.) Write a program that calculates the total cost of all the items in a shopping cart.
cart = [1.30, 5.62, 9.37, 11.32, 9.45, 7.86]
total = 0
for item in cart:
    total += item
print(f'Total Cost: ${total}')

print(sum(cart))  # This works too to count stuff.


########### Nested For Loops ###########
# Generate a list of coordinates that progress like this:
# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
#  ...

for x in range(6):
    for y in range(4):
        print(f'({x}, {y})')


#### Challenge: Make an F out of x's  ####

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    for count in range(number):
        print('x', end='')          # prints x 'number' times with for loop; end='' causes it to print on same line until it sees whitespace
    print('')                       # puts whitespace at the end of the previous line so that it creates a new line.

 # less complicated   #
numbers = [6, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for x in range(x_count):
        output += 'x'               # appending x's equal to the number of the current x_count
    print(output)                   # then printing that output before it gets set back to an empty string next time around

# Ex.) Make an "L"
numbers = [1, 1, 1, 6]
for x_count in numbers:
    output = ''
    for x in range(x_count):
        output += 'x'               # appending x's equal to the number of the current x_count
    print(output)                   # then printing that output before it gets set back to an empty string next time around
