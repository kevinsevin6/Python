# Unlike lists, we cannot modify tuples
numbers = (1, 2, 3)             # parenthesis instead of square brackets
#numbers.                       # typed this to see options:
                                # only have .count() and .index()
                                # the methods with _underscores_ are called magic methods. Not covered here.
print(numbers[0])
numbers[0] = 2                  # results in an error. Cannot modify

# If you want to create a list of items that you want to make sure never gets modified in any part of the code, then use
# a tuple.