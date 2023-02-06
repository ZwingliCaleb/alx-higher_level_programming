#!/usr/bin/python3
"""
contains function that adds attributes to existing objects
"""

def add_attribute(obj, att, value):
    """
        Args:
            obj (any): the object to add an attribute to
            att (str): The name of the attribute to add to obj
            value (any): the value of attr
        Raises:
            TypeError: if the attribute can not be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
