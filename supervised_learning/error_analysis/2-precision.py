#!/usr/bin/env python3
"""Calculates the precision for each class in a confusion matrix."""
import numpy as np


def precision(confusion):
    """function Calculates the precision"""
    TP = np.diag(confusion)
    # находишь диагональ на одной страке которая есть
    FP = np.sum(confusion, axis=0) - TP
    # из суммы по столбцу вычитаешь TP и получаешь FP
    precision = TP / (TP + FP)
    return precision
