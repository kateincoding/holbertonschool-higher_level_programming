#!/usr/bin/python3
"""
This is "matrix_divided" module

this module contains matrix_divided function,
that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Return division of all elements of the matrix given
    Arguments:
        matrix (list of list): first value to add
        div (int): int that will be used to divide

    Return:
        the division of al elements of a matrix
    """

    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) is 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    if size is 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) is not size:
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(b / div, 2) for b in i] for i in matrix]
