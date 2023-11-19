#!/usr/bin/env python3

"""
Rotate 2D Matrix
"""


def rotate(matrix):
    if not len(matrix) or len(matrix) != len(matrix[0]):
        return matrix
    n = len(matrix)
    n = len(matrix)
    for layer in range(n // 2):
        first, last, offset = layer, n - 1 - layer, 0
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            offset += 1
