#!/usr/bin/python3
"""The base class Module"""


class Base:
    """OOP heirachy representation of the base"""

    __nb__objects = 0

    def __init__(self, id=None):
        """Class Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
