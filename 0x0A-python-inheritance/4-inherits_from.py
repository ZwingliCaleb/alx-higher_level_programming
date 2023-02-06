#!/usr/bin/python3

""" module contains inherits_from function"""

def inherits_from(obj, a_class):
    """returns true if object is a subclass, else is false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
