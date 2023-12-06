#!/usr/bin/python3
"""Student representation module"""


class Student:
    """
    Defines student representation
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize an student's representation

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dict representation of student

        Returns:
            dict: dictionary containing the student's attributes
        """
        return (self.__dict__)
