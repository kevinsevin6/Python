course = "Python's Course for Beginners"    # using double quotes because of the apostrophe
print(course)

course = 'Python for "Beginners"'     # using single quotes so can use double in the string
print(course)

# multiple lines
course = '''To whom it may concern,
I am Kebin. 
This is my email.
THank you'''
print(course)

# Indexing
course = 'Python for beginners'
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:3])
print(course[0:])   # default end index is length of string
print(course[2:])
print(course[:4])   # default starting index is 0
print(course[:])
copy = course[:]
print('copy: ' + copy)

# Ex.) What will happen when you run the following code?

name = 'Jennifer'
print(name[1:-1])

# I think it will do 'ennife'
# Yay:)

###   Formatted Strings  ###

first = 'John'
last = 'Smith'
# print 'John [Smith] is a coder'
message = first + ' [' + last + '] is a coder'
print(message)

## Formatted ##
name = 'kebin'
type = 'the best'
msg = 'but ' + name + ' is ' + type + ' coder'
print(msg)
#   VS.   #
mesg = f'but {name} is {type} coder'     # much easier
print(mesg)