names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)

print(names[0])
print(names[2])
print(names[-1])
print(names[-2])
print(names[-0])       # still just prints the first name

print(names[2:])
print(names[2:4])
print(names[:3])       # assumes start index to be zero
# none of these will alter the names variable with the original list. It creates a new list.

# However, you can alter parts of the list if desired with the following:
names[0] = 'Jon'
print(names)
names[:2] = 'Kebin'    # fills in everything before the third name with the individual characters that make up 'Kebin'
print(names)

# Ex.) Write a program to find the largest number in a list.
list = [12, 34, 67, 89, -99, 28, 62]
largest = float('-inf')
for number in list:
    if number > largest:
        largest = number
print(f'WHOA! This is the highest number: {largest}')

# Oh, duh. No need to do negative infinity
list = [12, 34, 67, 89, -99, 28, 62]
largest = list[0]
for number in list:
    if number > largest:
        largest = number
print(f'WHOA! This is the highest number: {largest}')


############# 2D Lists  ##################

# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0])
print(matrix[0][0])
print(matrix[1][0])
print(matrix[2][2])

# Modifying
matrix[1][1] = 100
print(matrix[1][1])
print(matrix)

# Iterating over all the items in a loop
for row in matrix:
    for item in row:
        print(item)



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
numbers.pop()                           # removes the last item in the list
print(numbers)
numbers.clear()
print(numbers)

numbers = [10, 2, 1, 7, 20]
print(numbers.index(1))
#print(numbers.index(12))                # results in an error saying 12 is not in the list
print(50 in numbers)                     # doesn't stop your code with an error
check = 2 in numbers
print(check)


















