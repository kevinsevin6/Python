######## List Methods  (List functions) ##########

numbers = [5, 2, 1, 7 ,4]
numbers.append(20)                      # adds to the end of the list
print(numbers)
numbers.insert(1, 10)    # inserts an object (2nd field) at the specified index (1st field)
print(numbers)
numbers.remove(5)                       # removes the object specified
print(numbers)
numbers.remove(4)
print(numbers)
#numbers.remove(11)                     # causes an error and stops the code
print(numbers)
numbers.pop()                           # removes the last item in the list
print(numbers)
numbers.clear()
print(numbers)

numbers = [10, 2, 1, 7, 20]
print(numbers.index(1))
#print(numbers.index(12))                # results in an error saying 12 is not in the list
print(50 in numbers)                     # creates a boolean - doesn't stop your code with an error
check = 2 in numbers                     # can store this boolean in variables
print(check)

print(numbers.count(5))                  # counts how many times that item appears in list
print(numbers.count(2))
letters = ['b', 'c', 'a', 'c', 'd']      # wanted to see it work with strings
print(letters.count('c'))
print(numbers.sort())                    # result says "None" - None is an object in Python that represents the absense of a value
                                         # this is because sort() does not have a return value, it just orders the list in ascending order
print(numbers)                           # whoa, sort() still sorted even though I put it in print()
letters.sort()
print(letters)                           # whoa, it also puts strings in alphabetical order
letters.reverse()                        # to make it descending order
print(letters)

letters_2 = letters.copy()               # .copy() makes a copy of whatever you put it on
letters.append('kebin')                  # Then you can still have a copy of the original list while you change around the original list
print(letters)
print(letters_2)

# Ex.) Write a program to remove the duplicates in a list.
list = [2, 4, 6, 45, 7, 34, 7, 4, 7, 4, 3]
print(list)
for item in list:
   if list.count(item) > 1:
       list.remove(item)
print(list)

# If you want to keep original and create a new list without the duplicates
list = [2, 4, 6, 45, 7, 34, 7, 4, 7, 4, 3]
uniques = []
print(list)
for item in list:
   if item not in uniques:
       uniques.append(item)
print(uniques)