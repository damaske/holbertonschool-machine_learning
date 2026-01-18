#!/usr/bin/env python3
"""
 calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    calculates the derivative of a polynomial
    """
    if not isinstance(poly, list):
        return None
    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    if len(poly) == 0:
        return None

    der = [i * poly[i] for i in range(1, len(poly))]
    if not any(der):
        return [0]
    return der
