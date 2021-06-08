#!/usr/bin/python3
"""
Test differents behaviors of the Rectangle Class
"""
import unittest
import pep8
from io import StringIO
import os
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle_creation(unittest.TestCase):
    """A class to test Rectangle Class"""
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def set_up(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """Test for positive Base Class id"""
        self.set_up()
        r1 = Rectangle(10, 2)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        r2.id = 2
        self.assertEqual(r2.id, 2)

    def test_rectangle_instance(self):
        """Test if Rectangle is instance of Base"""
        r = Rectangle(5, 2, 1, 2, 20)
        self.assertEqual(type(r), Rectangle)
        self.assertTrue(type(r) == Rectangle)
        self.assertFalse(type(r) == Base)
        self.assertTrue(isinstance(r, Base))
        self.assertTrue(isinstance(r, Rectangle))

    def test_given_id(self):
        """Test fora given id"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_wrong_argumments(self):
        """Test for wrong argumments"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(5)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, 4, 5, 6, 7)


class Test_Rectangle_Attributes(unittest.TestCase):
    """A class to test attributes of Rectangle Class"""

    def set_up(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_correct_set_att(self):
        """test if the class catch the correct attributes"""
        r = Rectangle(10, 5, 1, 2, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 12)

    def test_input_not_integer(self):
        """Test if input is not an integer"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2 = Rectangle(10, 2)
            r2.x = {}

    def test_width_height_morethan0(self):
        """Test if width or height > 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(10, 2)
            r3.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(10, 5)
            r4.height = -10

    def test_x_y_more_equal_than0(self):
        """Test if x or y >= 0"""
        self.set_up()
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5 = Rectangle(10, 2, 3, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r5 = Rectangle(10, 2, -3, -1)

    def test_private(self):
        """Test the class if we try to do a private att"""
        self.set_up()
        r6 = Rectangle(10, 2, 3, 1)
        self.assertEqual(r6.x, 3)
        with self.assertRaises(AttributeError):
            r6.__x


class Test_Rectangle_Area(unittest.TestCase):
    """A class to test area of the Rectangle"""

    def set_up(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_area(self):
        """test area"""
        self.set_up()
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1.width = 5
        self.assertEqual(r1.area(), 10)

    def try_wrong_case(self):
        """when a size can be 0 but it is not possible"""
        self.set_up()
        r2 = Rectangle(3, 1)
        self.assertEqual(r2.height, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.height = 0


class Test_Display_noxnoy(unittest.TestCase):
    """Test display of Rectangle"""

    def set_up(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def display_rectangle(self):
        """check if rectangle prints
        case: no x neither y"""
        r1 = Rectangle(3, 3)
        with patch('sys.stdout', new=StringIO()) as draw12:
            self.assertEqual(draw12.getvalue(), "###\n###\n###\n")

    def display_line(self):
        """check if one size is 1
        case: no x neither y"""
        r2 = Rectangle(3, 1)
        with patch('sys.stdout', new=StringIO()) as draw12:
            self.assertEqual(draw12.getvalue(), "###\n")


class Test_str(unittest.TestCase):
    """Test the overriding str method"""

    def check_correct_print(self):
        """check if the method has an ok print"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1_result = "[Rectangle] (12) 2/1 - 4/6"
        with patch('sys.stdout', new=StringIO()) as string12:
            self.assertEqual(string12.getvalue(), r1_result)
        r2 = Rectangle(5, 5, 1)
        r2_result = "[Rectangle] (1) 1/0 - 5/5"
        with patch('sys.stdout', new=StringIO()) as string12:
            self.assertEqual(string12.getvalue(), r2_result)

    def check_change_att(self):
        """check if print changed"""
        r3 = Rectangle(7, 1, 1, 2, 3)
        r3_result = "[Rectangle] (3) 1/2 - 7/1"
        with patch('sys.stdout', new=StringIO()) as string13:
            self.assertEqual(string13.getvalue(), r3_result)
        r3.id = 5
        r3.x = 0
        r3.y = 0
        r3.width = 7
        r3.height = 7
        r3_new_result = "[Rectangle] (5) 0/0 - 7/7"
        with patch('sys.stdout', new=StringIO()) as string14:
            self.assertEqual(string14.getvalue(), r3_new_result)


class Test_Display(unittest.TestCase):
    """Test class for display method"""

    def set_nb_to_zero(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_valid_attrs(self):
        """Valid attrs for rectangle"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_invalid_attrs(self):
        """Invalid attrs for rectangle"""
        self.set_nb_to_zero()
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 1, -2)
            r1.display()

    def test_call_dispal_with_args(self):
        """pass 1 arg to display"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        with self.assertRaises(TypeError):
            r1.display(1)


class Test_Update(unittest.TestCase):
    """Test class for update method"""

    def set_nb_to_zero(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_0_args(self):
        """pass no args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update()
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 10)

    def test_1_args(self):
        """pass 1 arg to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100)
        self.assertEqual(r1.id, 100)

    def test_2_args(self):
        """pass 2 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)

    def test_3_args(self):
        """pass 3 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)

    def test_4_args(self):
        """pass 4 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)

    def test_5_args(self):
        """pass 5 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400, 500)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)
        self.assertEqual(r1.y, 500)

    def test_more_than_5_args(self):
        """pass 5 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400, 500, 600, 700, 800)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)
        self.assertEqual(r1.y, 500)

    def test_id_kwargs(self):
        """pass id kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123)
        self.assertEqual(r1.id, 123)

    def test_width_kwargs(self):
        """pass id width kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)

    def test_height_kwargs(self):
        """pass id width height kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)

    def test_x_kwargs(self):
        """pass id width height x kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432, x=940)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)
        self.assertEqual(r1.x, 940)

    def test_y_kwargs(self):
        """pass id width height x kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432, x=940, y=758)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)
        self.assertEqual(r1.x, 940)
        self.assertEqual(r1.y, 758)

    def test_more_kwargs(self):
        """pass valid and not valid kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432, x=940,
                  y=758, other='random', ok='rand val')
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)
        self.assertEqual(r1.x, 940)
        self.assertEqual(r1.y, 758)
        string = "'Rectangle' object has no attribute 'other'"
        with self.assertRaisesRegex(AttributeError, string):
            self.assertEqual(r1.other, 'random')
        string2 = "'Rectangle' object has no attribute 'ok'"
        with self.assertRaisesRegex(AttributeError, string2):
            self.assertEqual(r1.ok, 'rand val')

    def test_args_and_kwargs(self):
        """pass args and kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(129, 234, id=123, width=987, height=432,
                  x=940, y=758, other='random', ok='rand val')
        self.assertEqual(r1.id, 129)
        self.assertEqual(r1.width, 234)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 0)
        string3 = "'Rectangle' object has no attribute 'other'"
        with self.assertRaisesRegex(AttributeError, string3):
            self.assertEqual(r1.other, 'random')
        string4 = "'Rectangle' object has no attribute 'ok'"
        with self.assertRaisesRegex(AttributeError, string4):
            self.assertEqual(r1.ok, 'rand val')

    def test_1_args_invalid(self):
        """pass 1 invalid arg to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)

        # pass neagative int
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1.update(100, -23)

        # pass str
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1.update(321, 'randval')

        # pass float to update height
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1.update(28, 3, 23.43, 342)

        # pass bool to update x
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1.update(28, 3, 23, True)

    def test_args_as_iterable_obj(self):
        """pass iterable args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)

        # pass list to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = [1, 2, 3]
            r1.update(2, ls)

        # pass tuple to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = (1, 2, 3)
            r1.update(2, ls)

        # pass set to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = {1, 2, 3}
            r1.update(2, ls)

        # pass dict to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = {'width': 1, 'x': 2, 'y': 3}
            r1.update(2, ls)

    def test_args_invalid(self):
        """pass 2 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r1.update(100, 200, -43)

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r1.update(100, 200, 903, 23, -43)

        # invalid last arg passes because is not taken into account
        r1.update(100, 200, 903, 23, 345, 49, -43)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 903)
        self.assertEqual(r1.x, 23)
        self.assertEqual(r1.y, 345)


class Test_Dictionary_Representation(unittest.TestCase):
    """Test case class for update function"""
    def set_nb_to_zero(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_pass_1_arg(self):
        """Pass one argument to function call"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0, 1)
        self.assertEqual(r1.id, 1)
        string10 = "takes 1 positional argument but 2 were given"
        with self.assertRaisesRegex(TypeError, string10):
            r1.to_dictionary(239)

    def test_ret_dict(self):
        """Test to_dictionary function"""
        r1 = Rectangle(23, 43, 129, 32, 2)
        self.assertEqual(2, r1.id)
        d_comp = {'id': 2, 'width': 23, 'height': 43, 'x': 129, 'y': 32}
        self.assertDictEqual(r1.to_dictionary(), d_comp)

    def test_dict_with_args(self):
        """Test to_dictionary function"""
        r1 = Rectangle(10, 2, 1, 9, 9)
        r1_dict = r1.to_dictionary()
        d = {'x': 1, 'y': 9, 'id': 9, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dict, d)

        self.assertEqual(type(r1_dict), dict)

        r2 = Rectangle(10, 2, 1, 9, 10)
        r2_dict = r2.to_dictionary()
        d = {'x': 1, 'y': 9, 'id': 10, 'height': 2, 'width': 10}
        self.assertDictEqual(r2_dict, d)

        self.assertEqual(r1 == r2, False)


class TestRectangle(unittest.TestCase):
    """Test the functionality of the Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, True)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_str(self):
        """Test the str method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")
