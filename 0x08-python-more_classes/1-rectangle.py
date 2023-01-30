#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """Represent a rectangle"""
    def __init___(self, width=0, height=0):
        """Initialization of a new triangle
        Args:
            width (int): The width of new triangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self__height = value
