#################   Comparison Operators   #################
#                   <, >, >=, <=, ==, !=

# ex.) If temp greater than 30, hot day. Otherwise if less than 10, cold day. Otherwise neither hot or cold.
temp = 15
if temp > 30:
    print("It's hot!")
elif temp < 10:
    print("It's cold!")
elif temp == 15:
    print("IT'S 15 deg C!!")
else:
    print("Oo that's nice:)")

#ex.) Name must be between 3 and 50 characters long
name = input('Enter username: ')
if len(name) <= 2:   # Or just < 3
    print("Name must be at least 3 characters long.")
elif len(name) >= 16:   # Or just > 15
    print("Name length cannot be more than 15 chracters")
else:
    print("Nice username homie")