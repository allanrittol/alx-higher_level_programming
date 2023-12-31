#!/usr/bin/python3

"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of Class rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the prvate instance attribute width,"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            self.__height = value
