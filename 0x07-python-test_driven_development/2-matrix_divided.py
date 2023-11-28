#!/usr/bin/python3
"""
The modlule "2-matrix_divided.py"
A function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
            matrix (list): the matrix to divide it's elements
            div (_type_): num to divide by

    Returns:
            list: new list with result of division of each
            element in the matrix
    """

    directions = (
        "matrix must be a matrix (list of lists) of integers/floats",
        "Each row of the matrix must have the same size",
        "div must be a number",
        "division by zero"
    )
    length = [0, 0]
    result = []
    if not isinstance(matrix, list):
        raise TypeError(directions[0])
    length[0] = len(matrix)
    if length[0] == 0:
        raise TypeError(directions[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(directions[0])
        elif len(row) == 0:
            raise TypeError(directions[0])
        else:
            if length[1] == 0:
                length[1] = len(row)
            elif len(row) != length[1]:
                raise TypeError(directions[1])
            for colomn in row:
                if not isinstance(colomn, (int, float)):
                    raise TypeError(directions[0])
    if not isinstance(div, (int, float)):
        raise TypeError(directions[2])
    elif div == 0:
        raise ZeroDivisionError(directions[3])
    else:
        for row in matrix:
            resultRow = list(map(lambda x: round(x / div, 2), row))
            result.append(resultRow)
        return (result)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
