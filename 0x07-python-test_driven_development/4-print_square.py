#!/usr/bin/python3
"""Module "4-print_square.py". """


def print_square(size):
    """Method that prints a square with the character #.

    Args:
        size: The integer size of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
