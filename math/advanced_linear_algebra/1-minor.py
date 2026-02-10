#!/usr/bin/env python3
"""calculates the minor matrix of a matrix"""

def minor(matrix):
    """function that calculates the minor matrix of a matrix"""
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if matrix == [[]]:
        return 1
    minor_matrix = []
    for i in range(len(matrix)):
        minor_row = []
        for j in range(len(matrix)):
            sub_matrix = [row[:j] + row[j + 1:] for row in matrix[:i] + matrix[i + 1:]]
            minor_row.append(determinant(sub_matrix))
        minor_matrix.append(minor_row)
    return minor_matrix
