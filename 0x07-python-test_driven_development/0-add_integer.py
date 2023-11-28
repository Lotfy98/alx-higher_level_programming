#!/usr/bin/python3
"""
The "0-add_integer" module

"""


def add_integer(a, b=98):
    """
    Returns addition result of two integers

    Parameters:
        a (int, float): The first number.
        b (int, float): The second number (default 98).

    Returns:
        addition result of two integers

    Raise:
        TypeError: If one is not an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
