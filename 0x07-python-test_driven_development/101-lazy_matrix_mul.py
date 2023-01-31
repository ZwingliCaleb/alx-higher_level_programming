#!/usr/bin/python3
"""Defines a matrix multiplication function"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of two matrices
    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix
    """

    return (np.matmul(m_a, m_b))
