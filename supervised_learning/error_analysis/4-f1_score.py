#!/usr/bin/env python3
"""Calculate the F1 score for each class in a confusion matrix."""
import numpy as np


def f1_score(confusion):
    """function Calculates the F1 score"""
    TP = np.diag(confusion)
    FP = np.sum(confusion, axis=0) - TP
    FN = np.sum(confusion, axis=1) - TP
    precision = TP / (TP + FP)
    sensitivity = TP / (TP + FN)
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity)
    return f1_score
