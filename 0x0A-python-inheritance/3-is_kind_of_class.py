#!/usr/bin/python3
"""
Module contains is_kind_of_class function
"""

def is_kind_of_class(obj, a_class):
    """returns true if object is an instance/inherited from a class, else false"""
    return (isinstance(obj, a_class))
