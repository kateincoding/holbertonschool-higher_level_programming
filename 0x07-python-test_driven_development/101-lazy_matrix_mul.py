#!/usr/bin/python3
"""import numpy and define the module of lazy_matrix_mul"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrix with numpy
    Arguments:
        - m_a: matrix1
        - m_b: matrix2
    """
    return (np.matmul(m_a, m_b))
