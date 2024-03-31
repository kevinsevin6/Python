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