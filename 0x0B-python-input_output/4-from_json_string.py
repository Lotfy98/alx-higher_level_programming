#!/usr/bin/python3
"""JSON deserialze module"""


import json


def from_json_string(my_str):
    """
    Returns the python object as JSON string

    Args:
        my_str (str): the json string to be deserialized

    Returns:
        object: pythond DS represented by JSON string
    """
    return (json.loads(my_str))
