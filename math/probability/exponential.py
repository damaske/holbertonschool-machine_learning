#!/usr/bin/env python3
"""Exponential distribution."""


class Exponential:
    """Represents an exponential distribution."""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if isinstance(data, list):
                if len(data) < 2:
                    raise ValueError("data must contain multiple values")
                else:
                    delta = sum(data) / len(data)
                    self.lambtha = float(1/delta)
            else:
                raise TypeError("data must be a list")

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period."""
        if x < 0:
            return 0
        else:
            e = 2.7182818285
            return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """Calculates the value of the CDF for a given time period."""
        if x < 0:
            return 0
        else:
            e = 2.7182818285
            return 1 - (e ** (-self.lambtha * x))
