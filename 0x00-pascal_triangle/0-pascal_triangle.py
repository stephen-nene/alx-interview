#!/usr/bin/python3
"""
This module defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: 
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, len(triangle[-1])):
            # Append the sum of two elements above the current position
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
