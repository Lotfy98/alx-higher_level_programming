#!/usr/bin/python3
"""JSON save to file module"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
        my_obj: object to be serialized to JSON.

        filename (str): file where JSON will be saved

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dumps(my_obj, f)
