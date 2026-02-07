#!/usr/bin/env python3
"""code that calculates the determinant of a matrix"""
import numpy as np


def determinant(matrix):
    """function that calculates the determinant of a matrix"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("matrix must be square")
    return np.linalg.det(matrix)
