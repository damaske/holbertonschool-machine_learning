#!/usr/bin/env python3
"""Calculates the specificity for each class in a confusion matrix."""
import numpy as np


def specificity(confusion):
    """function Calculates the specificity"""
    TP = np.diag(confusion)
    # находишь диагональ на одной страке которая есть
    FP = np.sum(confusion, axis=0) - TP
    # из суммы по столбцу вычитаешь TP и получаешь FP
    FN = np.sum(confusion, axis=1) - TP
    # из суммы по строке вычитаешь TP и получаешь FN
    TN = np.sum(confusion) - (FP + TP + FN)
    # из общей суммы вычитаешь FP, TP и FN и получаешь TN
    specificity = TN / (TN + FP)
    return specificity
