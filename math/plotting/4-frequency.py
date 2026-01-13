#!/usr/bin/env python3
"""
This module plots a histogram of student grades
"""
import numpy as np
import matplotlib.pyplot as plt

def frequency():
    """
    This function plots histogram of student grades
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title("Project A")
    plt.hist(student_grades, bins=10, range=(0, 100), edgecolor='black')
    plt.show()
    