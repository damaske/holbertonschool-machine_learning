#!/usr/bin/env python3
"""code  that adds two matrices element-wise"""

def add_matrices2D(mat1, mat2):
    """function adds matrices elements"""
    new_mat = []

    if len(mat1[0]) != len(mat2[0]):
        return None
    for i in range(len(mat1)):
        row1 = len(mat1)
        row2 = len(mat2)
    if isinstance(row1, list) and isinstance(row2, list):
        if len(row1) != len(row2):
            return None
        new_row = []

        for j in range(len(row1)):
            new_row.append(row1[j] + row2[j])

        new_mat.append(new_row)

    return new_mat

