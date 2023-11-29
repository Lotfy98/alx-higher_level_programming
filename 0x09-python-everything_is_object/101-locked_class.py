#!/usr/bin/python3
"""101-locked_class Module
"""


class LockedClass:
    """Class that prevents user from
    creating objects
    """
    __slots__ = ['first_name']
