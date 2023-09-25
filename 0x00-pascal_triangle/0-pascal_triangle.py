#!/usr/bin/python3

def pascal_triangle(n):
    """Function that returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n > 0:
        re = []
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = int(C * (i - j) / j)
            re.append(level)
        return re
