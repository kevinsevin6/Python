def greet_user():
    print('Hi there!')
    print('Welcome aboard!')
# the only way lines of code in a function get executed is if the function is called

print("Start")
greet_user()
print("Finish")

### Parameters ###
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard!')

greet_user("Kebin")
greet_user("Edward")
# without a function, you would have to rewrite that code every time for each different name

# greet_user()                  # Running it without the parameter being specified will give you an error

# Definitions:
# parameters - the placeholders (like 'name') for functions
# arguments - the actual information given to the placeholders

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')

greet_user('Kebin', 'Sebin')    # multiple parameters
#greet_user('Kebin')                               # Error: missing 1 parameter or something

######## Keyword Arguments ##########
# position, or order, matters in the functions above
# These are called positional arguments
#greet_user("Sevin", first_name="Kebin")   # Error: got multiple values for argument 'first_name'
greet_user(last_name="Sevin", first_name="Kebin")       # Sweet. It worked.
                                                        # sometimes helps readability of the code, like if passing a bunch of numerical values to a function
def calc_cost(total, shipping, discount):
    dis = (total + shipping) * discount
    cost = total + shipping - dis
    print(cost)

#calc_cost(50, 5, 0.1)                                   # have no idea what these numbers are
calc_cost(total=50, shipping=5, discount=0.1)            # can tell what stuff is

# So, for the most part use positional arguments. But when taking numerical values, use keyword to make more readable
# But keyword arguments should always come after positional arguments!
#greet_user(first_name="kevin", "sevin")                  # causes error: pos argument follows keyword argument
                                                         # Also positional have to be in correct order and cannot have a keyword argument specifying it later, or it will try to put more than one value to the parameter and error
                                                         # so really keyword arguments should only be used as descriptors if mixing keyword and positional

####### Return Statement ############
def square(number):
    return number * number

square(3)                               # didn't print anything in the terminal
# Yoooooooo, so it doesn't mean it returns as in prints something out on the terminal
# It returns as in that process results in a value that you can now store somewhere if you want!!!!
answer = square(3)
print(answer)
# or
print(square(6))

# Oh wow, if you try to print a function that doesn't have a return statement, it will just print 'None' to the terminal
# because it only sees the function, not the code inside, and the function resulted in nothing.
def square(number):
    print(number * number)

print(square(4))                # printed the number when it came across the print function in the code, then 'None' for the result of the function
