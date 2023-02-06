#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""

class BaseGeometry:
    """A class with public instance methods area and integer validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than o"""
        if type(value) is not int:
            raise TypeError("{:s}} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """representation of rectangle"""
    def __init__(self, width, height):
        """rectangle instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """informal representation of rectangle in string format"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

class Square(Rectangle):
    """square representation"""
    def __init__(self, size):
        """square instantiation"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def are(self):
        """return area of square"""
        return self.__size ** 2

    def __str__(self):
        """string representation of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
