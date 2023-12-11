#!/usr/bin/python3
'''Module for Base class.'''
import csv
from json import dumps, loads
from os import path
from models.rectangle import Rectangle
from models.square import Square


class Base:
    '''A representation of the base of our OOP hierarchy.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary.'''
        return dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies a dictionary.'''
        return loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        list_objs = [o.to_dictionary() for o in list_objs] if list_objs else []
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        new = Rectangle(1, 1) if cls is Rectangle else Square(
            1) if cls is Square else None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        file = f"{cls.__name__}.json"
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        if list_objs is not None:
            list_objs = [[o.id, o.width, o.height, o.x, o.y] for o in list_objs] if cls is Rectangle else [
                [o.id, o.size, o.x, o.y] for o in list_objs]
        with open(f'{cls.__name__}.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        ret = []
        with open(f'{cls.__name__}.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                d = {"id": row[0], "width": row[1], "height": row[2], "x": row[3], "y": row[4]} if cls is Rectangle else {
                    "id": row[0], "size": row[1], "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()
        time.sleep(5)
