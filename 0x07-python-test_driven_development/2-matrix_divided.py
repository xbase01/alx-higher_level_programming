#!/usr/bin/python3
"""
This is the "matrix_divided" module.

The matrix_divided module provides a function, matrix_divided(matrix, div),
which divides all elements in a given matrix by a specified divisor.

Functions:
    matrix_divided(matrix, div): Divides each element in the matrix by div.

Raises:
    TypeError: If the matrix is not a list of lists of integers/floats, or
               if the rows of the matrix have different sizes.
    TypeError: If the divisor (div) is not a number (integer or float).
    ZeroDivisionError: If the divisor (div) is zero.

Example:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_divided(matrix, 2)
    # result is [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for l in matrix:
        if type(l) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in l] for l in matrix]
