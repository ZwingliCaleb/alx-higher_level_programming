#!/usr/bin/python3
"""Contains class "Student" """


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = ag

    def to_json(self):
        """returns a dictionary representation of a student instance"""
        return self.__dict__
