#!/usr/bin/python3
"""JSON object module"""


import json


def load_from_file(filename):
    """
    Create object from JSON file

    Args:
        filename (str): name of file to be deserialized

    Returns:
        object: the python DS represented by the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return (json.load(f))
