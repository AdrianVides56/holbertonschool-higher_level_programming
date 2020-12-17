#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for i in matrix:
        matrix_2 += [list(map(lambda x: x ** 2, i))]
    return matrix_2
