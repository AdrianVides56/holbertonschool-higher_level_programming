#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
        [1, 2, 3],
        [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
matrix2 = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix2, 3))
