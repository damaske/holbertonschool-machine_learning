#!/usr/bin/env python3
"""Calculates the sensitivity from a confusion matrix."""
import numpy as np


def sensitivity(confusion):
    """function Calculates the sensitivity"""
    #TP = confusion[1][1]
    #FN = confusion[1][0]
    return confusion[1][1] / (confusion[1][1] + confusion[1][0])
