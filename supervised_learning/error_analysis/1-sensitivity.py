#!/usr/bin/env python3
"""Calculates the sensitivity from a confusion matrix."""
import numpy as np


def sensitivity(confusion):
    """function Calculates the sensitivity"""
    TP = np.diag(confusion)
    FN = np.sum(confusion, axis=1) - TP
    sensitivity = TP / (TP + FN)
    return sensitivity

