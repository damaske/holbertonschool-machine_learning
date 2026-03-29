#!/usr/bin/env python3
"""Creates a confusion matrix from the given labels and logits."""
import numpy as np


def create_confusion_matrix(labels, logits):
    """Creates a confusion matrix from the given labels and logits."""
    true_labels = np.argmax(labels, axis=1)

    #превращаем [0, 0, 1] в 2, [0, 1, 0] в 1 и т.д.
    predicted_labels = np.argmax(logits, axis=1)

    #предсказанные классы
    classes = labels.shape[1]

    #создаем матрицу размером (кол-во классов, кол-во классов) и заполняем ее нулями
    confusion_matrix = np.zeros((classes, classes))

    #берем истинные и предсказанные создаем пары
    for true_label, predicted_label in zip(true_labels, predicted_labels):
        #используем эти пары как кординаты в матрице и увеличиваем на единицу значение в этой ячейке
        confusion_matrix[true_label][predicted_label] += 1

    return confusion_matrix
