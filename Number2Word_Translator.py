# Ex.) Write a program that translates given numbers into words.

dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
phone = input("Yo, can I getcha digits? ")
output = ''
for item in phone:
    output += f'{dict.get(item, '')} '
print(output)
