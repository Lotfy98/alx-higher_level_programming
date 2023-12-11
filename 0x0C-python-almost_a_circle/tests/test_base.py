#!/usr/bin/python3
'''Module for testing the Base class.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''A class to test the Base class.'''

    def setUp(self):
        '''Set up for the test cases.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up after each test case.'''
        pass

    def test_A_nb_objects_private(self):
        '''Check if nb_objects is a private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Check if nb_objects is initialized to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Test instantiation of the Base class.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Test the constructor's signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Test the constructor's signature with two arguments.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Test if IDs are consecutive.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Test if the class and instance IDs are synchronized.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        '''Test if the class and instance IDs are synchronized with multiple instances.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Test if a custom integer ID is accepted.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Test if a custom string ID is accepted.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        '''Test if an ID passed as a keyword argument is accepted.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)
# ----------------- Tests for #15 ------------------------

    def test_H_to_json_string(self):
        '''Tests the to_json_string() method.'''
        # Test if the method raises a TypeError when no arguments are passed
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        # Test if the method returns an empty list when None or an empty list is passed
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test if the method correctly converts a list of dictionaries to a JSON string
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))

        # Test if the method correctly converts a list of dictionaries with different keys to a JSON string
        d = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}]')

        # Test if the method correctly converts a list of multiple dictionaries to a JSON string
        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        # Test if the method correctly converts a list of empty dictionaries to a JSON string
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        # Test if the method correctly converts a dictionary representation of a Rectangle instance to a JSON string
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        # Test if the method correctly converts a dictionary representation of multiple Rectangle instances to a JSON string
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        # Test if the method correctly converts a dictionary representation of a Square instance to a JSON string
        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        # Test if the method correctly converts a dictionary representation of multiple Square instances to a JSON string
        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    # ----------------- Tests for #17 ------------------------
    def test_H_test_from_json_string(self):
        '''Tests the from_json_string() method.'''
        # Test if the method raises a TypeError when no arguments are passed
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), s)

        # Test if the method returns an empty list when None or an empty string is passed
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        # Test if the method correctly converts a JSON string to a list of dictionaries
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(Base.from_json_string(s), d)

        # Test if the method correctly converts a JSON string of empty dictionaries to a list of dictionaries
        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)
# ----------------- Tests for #16 ------------------------

    def test_I_save_to_file(self):
        '''Tests the save_to_file() method.'''
        import os
        # Test if the method correctly saves a list of Rectangle instances to a file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        # Test if the method correctly handles None and empty lists
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        # Test if the method correctly saves a single Rectangle instance to a file
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        # Test if the method correctly saves a list of Square instances to a file
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        # Test if the method correctly saves a single Square instance to a file
        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    # ----------------- Tests for #18 ------------------------
    def test_J_create(self):
        '''Tests the create() method.'''
        # Test if the method correctly creates a new Rectangle instance from a dictionary
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    # ----------------- Tests for #19 ------------------------
    def test_K_load_from_file(self):
        '''Tests the load_from_file() method.'''
        # Test if the method correctly loads a list of Rectangle instances from a file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        # Test if the method correctly loads a list of Square instances from a file
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))


if __name__ == "__main__":
    unittest.main()
