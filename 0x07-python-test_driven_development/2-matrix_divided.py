#!/usr/bin/python3
"""
Creating a new function:

matrix_divided
"""


def matrix_divided(matrix, div):
    """matrix_divided - divides all elements of a matrix"""
    if type(matrix) is not list or len(matrix) <= 1:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not (all(isinstance(element, list) for element in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    if length == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    new_mtx = []
    for a in matrix:
        if type(a) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if length != len(a):
            raise TypeError("Each row of the matrix must have the same size")
        for b in a:
            if type(b) not in [int,float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                    of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        list_aux = []
        for j in i:
            list_aux.append(round((j / div), 2))
        new_mtx.append(list_aux)
    return new_mtx
