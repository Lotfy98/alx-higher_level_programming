#!/usr/bin/python3
"""JSON serialize module"""


def to_json_string(my_obj):
    """
    Reutrns the JSON representation of an object (str).

    Args:
        my_obj: the object to mbe serialized to JSON.

    Returns:
        str: JSON representation of the object.
    """
    return (json.dumps(my_obj))
