#!/usr/bin/python3
"""Append module"""


def appen_write(filename="", text=""):
    """
    Appends str at end of txt file and returns num of chars added

    Args:
        filename (str): name of file which text will be appended

        text (str): text which will be appended to fie

    Returns:
        int: num of chars appended to the file
    """
    with open(filename, mod='a', encoding='utf-8') as f:
        return (f.write(text))
