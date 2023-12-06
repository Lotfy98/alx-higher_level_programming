#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """Reads txt file (UTF-8) and prints to stdout

    Args:
        filename (str): the name of file to read

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
