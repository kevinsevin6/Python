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