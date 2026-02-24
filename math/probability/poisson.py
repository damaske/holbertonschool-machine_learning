#!/usr/bin/env python3
"""Poisson distribution"""


class Poisson:
    """Represents a poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if isinstance(data, list):
                if len(data) < 2:
                    raise ValueError("data must contain multiple values")
                else:
                    self.lambtha = float(sum(data) / len(data))
            else:
                raise TypeError("data must be a list")

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of “successes”"""
        if k < 0:
            return 0
        else:
            k = int(k)
            e = 2.7182818285
            factorial = 1
            for i in range(1, k + 1):
                factorial *= i
            return (self.lambtha ** k * e ** -self.lambtha) / factorial
