is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day!!")
print('Enjoy your day')

# If they are both set to true, it will see that the first one is true, run that code, and skip the elifs. So even if
# cold is set to true, it won't run them.
# If both are false, it goes to the else:

# Ex.) Price of a house is $1M. If buyer has good credit, 10% down. If not, 20% down.
house = 1000000
good_credit = True
if good_credit:
    down = house * 0.1
else:
    down = house * 0.2
print(f'Down payment is ${down}')


########   Logical Operators  #######
# AND
high_income = False
GOOD_credit = False

if high_income and GOOD_credit:
    print("Eligible for loan")
else:
    print("No loan:(")

# OR
if high_income or GOOD_credit:
    print("Well I guess")
else:
    print("Definitely not")

# NOT    -   reverses any boolean value
# ex.) If good credit and doesn't have a criminal record
good_CREDIT = True
criminal = False
if good_CREDIT and not criminal:
    print("yes")
else:
    print('no')


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