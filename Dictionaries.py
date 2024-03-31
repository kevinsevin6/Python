# Defined with curly braces
# You use dictionaries when you want a place to store key:value pairs
# like a list of customers info like name, email, phone, etc.

customer = {                                    # value can be anything: string, number, boolean, list
    "name": "John Smith",
    "age": 30,
#   "age": 45,                                  # not allowed to have duplicate keys
    "is_verified": True
}

print(customer["name"])
#print(customer["birthday"])                    # KeyError: 'birthday' - bc it does not exists
#print(customer["NAme"])                        # Same error bc case sensitive

print(customer.get("birthday"))                 # To avoid an error when doesn't exist or mistyped
                                                # Returns "None"
print(customer.get("age"))                      # Returns the value
print(customer.get("alias", "Kebin"))           # Can also give it a default value for if the key does not exist ?? When would you want to do that?
print(customer.get("name", "kebin"))            # If you give it a default value, but the key does exist, it gives you the dictionary value
                                                # Ooh, okay. So you can pull a key, and if it doesn't exist, then just report this default value.
customer["name"] = "Jack Smith"                 # update a value
print(customer["name"])
customer["birthday"] = "Jan 1, 2024"            # can add a new key
print(customer["birthday"])


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
