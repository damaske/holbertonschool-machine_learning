#!/usr/bin/env python3
"""function that show count rows and elements of rows"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix"""
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
