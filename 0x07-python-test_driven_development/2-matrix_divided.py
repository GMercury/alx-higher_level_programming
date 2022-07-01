#!/usr/bin/python3
""" 2-matrix_divided.py """


def is_valid_matrix(matrix):
    """Checks if a given matrix is a valid matrix of integers

    Args:
        matrix: matrix to be checked

    Returns: True if matrix is a valid matrix. Otherwise False
    """
    # check that matrix is a list and it's not empty
    if type(matrix) != list or len(matrix) == 0:
        return False

    # check that all elements of the matrix are lists of integers of same size
    if type(matrix[0]) != list:
        return False

    row_size = len(matrix[0])
    for row in matrix:
        # check that the current element is a list of the correct size
        if type(row) != list:
            return False
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # check that the current row only contains integers/floats
        for num in row:
            if type(num) not in [int, float]:
                return False

    return True


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number

    Args:
        matrix: list of lists of integers or floats
        div: number to divide matrix by

    Returns: new matrix containing result
    """
    # check that matrix is valid
    if not is_valid_matrix(matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    # check that div is valid
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]
