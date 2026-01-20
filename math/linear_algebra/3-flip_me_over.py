#!/usr/bin/env python3
"""function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """function transpose matrix"""
    transp = []

    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        transp.append(new_row)
    return transp
