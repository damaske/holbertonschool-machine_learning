#!/usr/bin/env python3
"""code that concatenates two matrices"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """finction that concatenates two matrices"""
    return np.concatenate((mat1, mat2), axis=axis)
