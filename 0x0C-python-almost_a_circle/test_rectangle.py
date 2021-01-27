#!/usr/bin/python3import unittest
""" Initializes module an import """
import json
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """ Class to test Rectangle """
    def test_regular_working(self):
        """ Correc working """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validate_attributes(self):
        """ Test for correct type of attributes """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, "2")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(10, 2, 3, -1)

    def test_area(self):
        """ Test area method """
        r11 = Rectangle(3, 2)
        self.assertEqual(r11.area, 6)

        r22 = Rectangle(2, 10)
        self.assertEqual(r22.area, 20)

        r33 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r33.area, 56)
