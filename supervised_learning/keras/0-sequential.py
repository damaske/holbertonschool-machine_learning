#!/usr/bin/env python3
""" Task 0: 0. Sequential """
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Builds a fully connected neural network using the Keras library.

    Parameters:

    nx : int
        The number of input features to the network.
    layers : list of int
        A list containing the number of nodes in each layer
        of the network.
    activations : list of str or callable
        A list containing the activation functions for
        each layer.
    lambtha : float
        The L2 regularization parameter (L2 penalty) for
        kernel weights.
    keep_prob : float
        The probability of keeping a node active during dropout
        (1 - dropout rate).

    Returns:
    model : keras.Sequential
        The constructed Keras model.
    """
    model = K.Sequential() #Создается пустая последовательная модель

    reg = K.regularizers.L1L2(l2=lambtha) # Создается объект регуляризации L2 с параметром lambtha

    #Первый слой создается отдельно, потому что только он должен знать размер входных данных (input_shape).
    model.add(K.layers.Dense(units=layers[0], #количество нейронов в первом слое
                             activation=activations[0], #функция активации для первого слоя activations = ["relu", "relu", "softmax"]
                             kernel_regularizer=reg,
                             input_shape=(nx,),)) # input_shape=(100,) (запятая что бы кортеджом стало)количество входных признаков nx

    #второй и длаее слои создаются в цикле, так как они не требуют указания input_shape
    for i in range(1, len(layers)): # для каждого слоя после первого
        model.add(K.layers.Dropout(1 - keep_prob)) # добавляется слой dropout
        model.add(K.layers.Dense(units=layers[i], #количество нейронов в i-м слое
                                 activation=activations[i], #функция активации для i-го слоя
                                 kernel_regularizer=reg,
                                 ))

    return model
