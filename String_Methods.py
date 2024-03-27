course = 'Python for beginners'
print(len(course))      # len() works on anything, not just strings
### There are general purpose functions that work on anything, and there are methods. Methods are specific to a certain
### type of object. General purpose functions are used like you might think, with parenthesis surrounding the variable
### being affected. Methods are attached to the variable or object being affected using dots:   variable.method()

# you can see all the functions (or methods) that are specific to strings by putting a dot after the variable containing a string
# when a function belongs to something else or is specific to some kind of object, it is called a method

print(course.upper())
print(course)     # ^ does not change the variable
print(course.lower())
print(course.title())    # capitalizes first letter of every word

# .find   -   shows the index of the first occurrence of the letter or word
#             shows -1 if it does not occur
print(course.find('P'))
print(course.find('o'))

# .replace
print(course.replace('beginners', 'absolute beginners'))
    # It is case sensitive. If what you give it does not exist, it will still print, just as is

# Check existance of a string, word, phrase, letter, etc.
print('beg' in course)
print('Beg' in course)