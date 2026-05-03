#!/usr/bin/env python3
""" Task 0: 0. Privatize Neuron"""
import numpy as np


class Neuron:
    """
    A class used to represent a single neuron in a neural network.

    Attributes
   __ W : numpy.ndarray
        The weight vector for the neuron
    __ b : float
        The bias for the neuron, initialized to 0.
    __ A : float
        The activation output of the neuron, initialized to 0.

    Methods
    __init__(self, nx)
        Initializes a neuron with `nx` input features.
    """
    def __init__(self, nx):
        """
        Initialize the Neuron instance.

        Parameters
        nx : int
            The number of input features to the neuron. It must be a
            positive integer.

        Raises
        TypeError
            If `nx` is not an integer.
        ValueError
            If `nx` is less than 1.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        else:
            self.__W = np.random.normal(0, 1, (1, nx))
            self.__b = 0
            self.__A = 0

    @property
    def W(self):
        """ Getter for the weight vector W. """
        return self.__W

    @property
    def b(self):
        """ Getter for the bias b. """
        return self.__b

    @property
    def A(self):
        """ Getter for the activation output A. """
        return self.__A
    
    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron.

        Parameters
        X : numpy.ndarray
            The input data for the neuron, with shape (nx, m), where
            nx is the number of input features and m is the number of
            examples.

        Returns
        A : numpy.ndarray
            The activation output of the neuron after forward propagation.
        """
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A
