#!/usr/bin/env python3
"""
Docstring for math.calculus.9-sum_total
"""


def summation_i_squared(n):
    """
    Calculate the sum of the squares of the first n natural numbers.
    """
    if n <= 0 or not isinstance(n, int):
        return None
    return n*(n + 1)*(2*n + 1)//6
