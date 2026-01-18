#!/usr/bin/env python3
"""
calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
     """
     calculates the integral of a polynomial
     
     :param poly: list of coefficients representing the polynomial
     :param C: constant of integration
     """
     if not isinstance(poly, list):
         return None
     if not all(isinstance(c, (int, float)) for c in poly):
         return None
     if len(poly) == 0:
         return [C] if C != 0 else None
     if not isinstance(C, (int, float)):
         return None
     
     poly_int = [C]
     
     for i, coef in enumerate(poly):
        coeff = coef / (i + 1)
        if coeff.is_integer():
            coeff = int(coeff)
        poly_int.append(coeff)
        
     while len(poly_int) > 1 and poly_int[-1] == 0:
        poly_int.pop()
            
     return poly_int
