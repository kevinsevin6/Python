########### Nested Loops ###########
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
