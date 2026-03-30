#!/usr/bin/env python3
"""Calculate the F1 score for each class in a confusion matrix."""
import numpy as np


def f1_score(confusion):
    """function Calculates the F1 score"""
    TP = np.diag(confusion)
    #находишь диагональ на одной страке которая есть
    FP = np.sum(confusion, axis=0) - TP
    #из суммы по столбцу вычитаешь TP и получаешь FP
    FN = np.sum(confusion, axis=1) - TP
    #из суммы по строке вычитаешь TP и получаешь FN
    precision = TP / (TP + FP)
    sensitivity = TP / (TP + FN)
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity)
    return f1_score
