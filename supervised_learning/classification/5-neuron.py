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
            # 0—среднее (центр около нуля), 1-разброс (стандартное отклонение),
            # (1, nx)—форма матрицы: 1 строка, nx столбцов
            # Просто создаёт случайные начальные веса.
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
        # dot Перемножает матрицы — это и есть W · X
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A
# Шаг 1: z = W · X + b   (взвешенная сумма)
# Шаг 2: A = σ(z)        (применяем сигмоид)

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression.

        Parameters
        Y : numpy.ndarray
            The correct labels for the input data, with shape (1, m).
        A : numpy.ndarray
            The activated output of the neuron for each example, with
            shape (1, m).

        Returns
        cost : float
            The cost of the model.
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m
        # sum -складывает всё в одно число (поэлементно)
        # np.log - логарифм каждого элемента,
        # 1.0000001 - это для избежания деления на ноль
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron’s predictions.

        Parameters
        X : numpy.ndarray
            The input data for the neuron, with shape (nx, m), where
            nx is the number of input features and m is the number of
            examples.
        Y : numpy.ndarray
            The correct labels for the input data, with shape (1, m).

        Returns
        prediction : numpy.ndarray
            The predicted labels for each example, with shape (1, m).
        cost : float
            The cost of the model.
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        # для каждого элемента A — если >= 0.5 то поставь 1, иначе 0
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neuron.

        Parameters
        X : numpy.ndarray
            The input data for the neuron, with shape (nx, m), where
            nx is the number of input features and m is the number of
            examples.
        Y : numpy.ndarray
            The correct labels for the input data, with shape (1, m).
        A : numpy.ndarray
            The activated output of the neuron for each example, with
            shape (1, m).
        alpha : float
            The learning rate for gradient descent.

        Returns
        None
        """
        m = Y.shape[1]  # количество примеров
        dZ = A - Y  # разница между предсказаниями и правильными метками
        dW = np.dot(dZ, X.T) / m  # градиент по весам, в какую сторону и насколько сильно менять вес.
        db = np.sum(dZ) / m  # градиент по смещению
        self.__W -= alpha * dW
        self.__b -= alpha * db
