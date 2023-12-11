#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return f'[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for attr, value in kwargs.items():
                if attr in attributes:
                    setattr(self, attr, value)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
