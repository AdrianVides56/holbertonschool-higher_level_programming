#!/usr/bin/python3
""" Initializes module an import """
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """ Class to test Base """
    def test_regular_working(self):
        """ Correct working """
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

        b2 = Base(2)
        self.assertEqual(b2.id, 2)

        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_too_many_arguments(self):
        """ Tests if more arguments were passed """
        with self.assertRaises(TypeError):
            b = Base(1, 2)

        with self.assertRaises(TypeError):
            b = Base('my_id', 2, 3)
