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
