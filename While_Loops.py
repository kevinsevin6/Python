i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")


i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

# Guessing Game
secret = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret:
        print('YAY!!')
        break
else:
    print('Booooo')

# Ex.) Car Game
# Just waiting on you to type something. Typing "help" tells shows you all your options.
# Options: start - starts the car; stop - stops the car; quit - exit game.

command = ''
car_status = 'stop'

while True:
    command = input('>').lower()
    if command == 'help':
        print('''
start - starts the car!
stop - stops the car
quit - exit the game
        ''')
    elif command == car_status and command == 'start':
        print('Click, click, click... the car is already started silly goose.')
    elif command == car_status and command == 'stop':
        print("Stop what? I'm not doing anything.")
    elif command == 'start':
        print('Vroom vrOOOOOOOOMMmmm')
    elif command == 'stop':
        print('Car is off.')
    elif command == 'quit':
        break
    else:
        print('Type "help" for a list of commands.')

    if command == 'start':
        car_status = command
    elif command == 'stop':
        car_status = command


# It feels dumb to use an if statement to break the while loop if they enter 'quit' because that's the whole point of
# the while loop itself. It will never have a chance to break itself. Is there a way to just skip the if statements if
# 'quit' is entered?
# ANSWER: Nevermind, he addressed this. Wow! You can just do while True!!!
# "while True" will just run forever until something in the loop explicitly breaks it.

# A cleaner way to do all these different things:

command = ''
car_status = 'off'

while True:
    command = input('>').lower()

    if command == 'help':
        print('''
start - starts the car!
stop - stops the car
quit - exit the game
        ''')
    elif command == 'start':
        if car_status == 'on':
            print("Click, click, click... I'm already started silly goose.")
        else:
            print('Vroom vrOOOOOOOOMMmmm')
            car_status = 'on'
    elif command == 'stop':
        if car_status =='off':
            print('Whoa man.')
        else:
            print('Car is now off.')
            car_status = 'off'
    elif command == 'quit':
        break
    else:
        print('Type "help" for a list of commands.')

##### Even cleaner #######

command = ''
started = False

while True:
    command = input('>').lower()

    if command == 'help':
        print('''
start - starts the car!
stop - stops the car
quit - exit the game
        ''')
    elif command == 'start':
        if started:
            print("Click, click, click... I'm already started silly goose.")
        else:
            print('Vroom vrOOOOOOOOMMmmm')
            started = True
    elif command == 'stop':
        if not started:
            print('Whoa man.')
        else:
            print('Car is now off.')
            started = False
    elif command == 'quit':
        break
    else:
        print('Type "help" for a list of commands.')