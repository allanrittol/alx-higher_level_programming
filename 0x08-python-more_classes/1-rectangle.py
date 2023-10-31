#!/usr/bin/python3

"""Description of the class"""


class Rectangle:
    """
    Class represents a rectangle, and has a private instance attribute width
    and height, with property setters and getters.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle with optional width and height
        """
        self.width = width
        self.height - height

        @property
        def width(self):
            """Retrieves the width of the Rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """
            sets the width of the Rectangle,
            Raise TypeError if width is not an integer,
            Raise Valueerror if width is less than 0
            """
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
