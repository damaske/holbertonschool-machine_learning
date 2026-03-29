#!/usr/bin/env python3
"""Creates a confusion matrix from the given labels and logits."""
import numpy as np

def create_confusion_matrix(labels, logits):
    """Creates a confusion matrix from the given labels and logits."""
    true_labels = np.argmax(labels, axis=1)
    predicted_labels = np.argmax(logits, axis=1)
    
    classes = labels.shape[1]
    confusion_matrix = np.zeros((classes, classes))

    for true_label, predicted_label in zip(true_labels, predicted_labels):
        confusion_matrix[true_label][predicted_label] += 1

    return confusion_matrix
