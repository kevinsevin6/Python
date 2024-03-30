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