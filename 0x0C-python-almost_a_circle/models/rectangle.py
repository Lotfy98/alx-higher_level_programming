#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.__set_values(width=width, height=height, x=x, y=y)

    def __set_values(self, **kwargs):
        '''Method to set values.'''
        for key, value in kwargs.items():
            if isinstance(value, int):
                if value > 0 or (value >= 0 and key in ['x', 'y']):
                    setattr(self, f'_{Rectangle.__name__}__{key}', value)
                else:
                    raise ValueError(f"{key} must be > 0")
            else:
                raise TypeError(f"{key} must be an integer")

    def area(self):
        '''Computes area of this rectangle.'''
        return self.__width * self.__height

    def display(self):
        '''Prints string representation of this rectangle.'''
        print('\n' * self.__y + (' ' * self.__x + '#' *
              self.__width + '\n') * self.__height, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return f'[{Rectangle.__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__set_values(id=args[0], width=args[1],
                              height=args[2], x=args[3], y=args[4])
        elif kwargs:
            self.__set_values(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}
