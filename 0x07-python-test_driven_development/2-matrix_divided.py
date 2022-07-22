#!/usr/bin/python3
"""
A function that divides the numbers of a matrix
"""
def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msgraised = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msgraised)

    len__ = 0
    msgsize = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements,list):
            raise TypeError(msgraised)

        if len__ != 0 and len(elements) != len__:
            raise TypeError(msgraised)

        len__ = len(elements)

        m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
        return (m)
