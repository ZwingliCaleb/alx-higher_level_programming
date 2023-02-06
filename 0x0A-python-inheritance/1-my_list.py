#!/usr/bin/python3

""" module: 1-my_list
"""

class MyList(list):
    """Subclass for main class -list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """list print function"""
        print(sorted(self))
