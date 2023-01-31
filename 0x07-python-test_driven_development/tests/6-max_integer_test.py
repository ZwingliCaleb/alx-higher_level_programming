#!/usr/bin/python3

''' Unit test for max_integer function
'''

import unittest
from importlib import import_module

class TestMaxInteger(unittest.TestCase):
    ''' test the funcion
    '''

    def test_area(self):
        '''Equality tests for the function
        '''

        max_integer = import_module('6-max_integer', '..').max_integer
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([7, 2, -3, 45, 6]), 45)
        self.assertEqual(max_integer([7, 2, 45, 6]), 45)
        self.assertEqual(max_integer([-7, -2, -45, -6]), -2)
        self.assertEqual(max_integer([-7, 1, -18, -6]), 1)
