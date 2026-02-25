#!/usr/bin/env python3
"""Binomial distribution module"""


class Binomial:
    """Binomial distribution class"""
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = 0
            for x in data:
                variance += (x - mean) ** 2
            variance /= len(data)
            p = 1 - (variance / mean) if mean != 0 else 0
            n = round(mean / p) if p != 0 else 0
            p = mean / n if n != 0 else 0
            self.n = int(n)
            self.p = float(p)

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes"""
        if k < 0 or k > self.n:
            return 0
        from math import factorial
        coeff = factorial(self.n) / (factorial(k) * factorial(self.n - k))
        return coeff * (self.p ** k) * ((1 - self.p) ** (self.n - k))
