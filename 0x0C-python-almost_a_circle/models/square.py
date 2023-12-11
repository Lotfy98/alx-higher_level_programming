#!/usr/bin/python3
'''This module defines the Square class,
which inherits from the Rectangle class.
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''This class represents a Square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor for the Square class.
        Initializes size, x, y, and id.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns a string representation of the square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Getter for the size attribute.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for the size attribute. Also sets
        the width and height to the same value.
        '''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes
        using positional or keyword arguments.
        '''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes using
        positional or keyword arguments.
        '''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns a dictionary representation of the Square instance.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
