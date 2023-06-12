#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for x in matrix:
        result.append(list(map(lambda x: x**2, x)))
    return (result)
