#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    nm = list(map((lambda x: x **2), matrix))
    print(nm)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
            ]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

