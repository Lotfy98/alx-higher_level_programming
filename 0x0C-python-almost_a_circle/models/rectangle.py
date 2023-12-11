#!usr/bin/python3
"""Rectangle class module"""
from models.base import Base


def validInt(value, attr, minValue=None, eq=False):
    """Validating integer"""
    if not isinstance(value, int):
        raise TypeError(f"{attr} must be >= {minValue}")
    if minValue is not None:
        if eq and value < minValue:
            raise ValueError(f"{attr} must be >= {minValue}")
        elif not eq and value <= minValue:
            raise ValueError(f"{attr} must be > {minValue}")


def area(self):
    """Calculate and return the area"""
    return (self.__width * self.__height)


def display(self):
    """Print rectangle using # character"""
    print("\n" * self.__y, end="")
    for _ in range(self.__height):
        print(" " * self.__x + "#" * self.__width)


def __str__(self):
    """Returns string of rectangle instances"""
    return "[Rectangle] ({}) {}/{} - {}/{}".\
        format(self.id, self.__x, self.__y, self.__wifth, self.__height)


class Rectangle(Base):
    """Rectangle class inheriting from another class called Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        validInt(width, "width", 1)
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        validInt(height, "height", 1)
        self.__height = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        ValidInt(x, "x", 0)
        slef.__x = x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        validInt(y, "y", 0)
        self.__y = y
