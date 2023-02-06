#!/usr/bin/python3
"""
contains MyInt class
"""

class MyInt(int):
    """opposite version of integer"""
    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """inverted '!=' and '==' """
        return int(self) != other

    def __ne__(self, other):
        """reversed inversion"""
        return int(self) == other
