#!/usr/bin/env python3
"""function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """def cat_matrices2D(mat1, mat2, axis=0)"""
    if axis != 0:
        return None

    if len(mat1[0]) != len(mat2[0]):
        return None

    new_mat = []

    for row in mat1:
        new_mat.append(list(row))

    for row in mat2:
        new_mat.append(list(row))

    return new_mat

