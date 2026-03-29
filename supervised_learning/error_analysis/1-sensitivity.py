#!/usr/bin/env python3
"""Calculates the sensitivity from a confusion matrix."""
import numpy as np


def sensitivity(confusion):
    """function Calculates the sensitivity"""
    TP = np.diag(confusion)
    #находишь диагональ на одной страке которая есть 
    FN = np.sum(confusion, axis=1) - TP
    #из суммы по строке вычитаешь TP и получаешь FN
    sensitivity = TP / (TP + FN)
    return sensitivity
