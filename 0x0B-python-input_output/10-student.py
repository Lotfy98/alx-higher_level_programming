class Student:
    """
    Defines a student with public instance attributes and methods.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student object with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of strings representing attribute names to retrieve.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            # Only retrieve attributes specified in the attrs list
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            # Retrieve all attributes
            return self.__dict__
