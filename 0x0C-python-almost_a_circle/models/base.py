#!/usr/bin/python3
"""Base module"""


class Base:
    """An OOP hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization constructor"""
        if id is None:
            """Assign input"""
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
