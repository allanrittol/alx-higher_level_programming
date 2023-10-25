#!/usr/bin/python3


class Square:
    """This is a class that defines a Square."""

    def __init__(self, size=0):
        """This is the constructor method for Square class.
        The size must be an integer, otherwise

        Raise: A TypeError exception with the message size
        must be an integer.
        If size is less than 0, raise a ValueError exception
        with the message size must be >= 0.
        """
        self.size = size

        @property
        def size(self):
            """Get/set the current size of the square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        def area(self):

            return self.__size ** 2
