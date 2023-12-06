#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """
    Write str to txt file and return num of chars written

    Args:
        filename (str): the file where text will be written

        text (str): the text to be written t the file

    Returns:
        int: num of characters written to the file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return (f.write(text))
