name = input('What is your name? ')   # he said whenever we put the parenthesis, this is what causes it to call the function
print(name)
print('Hi ' + name)    # this is another expression that produces a a value he says

# Ex.) Ask two questions, name and favorite car

Name = input('Hi! What is your name? ')
car = input('Hi ' + Name + '! ' + 'What is your favorite kind of car? ')
print(name + "'s favorite car is a " + car)


# Ex.) Ask what year they were born, calculate age.

birth_year = input('Hi! What year were you born? ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(birth_year))
print(type(age))
print("Wow!! You're " + str(age) + '???')

#CONVERSIONS
# int()
# float()
# bool()
# str()

# Ex.) Ask user what their weight is (lbs), convert to kg.

wt_lbs = input("I don't mean to be rude, but how much do you weigh? ")
kg = int(wt_lbs) * 0.4536
print('That would be ' + str(kg) + ' if you were British!')
