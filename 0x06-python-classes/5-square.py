#!/usr/bin/python3


class Square:
    """
    This is a Square class that defines a square by a
    private instance attribute: size.
    """
    def __init__(self, size=0):
        """
        This is the constructor method for Square class.
        The size must be an integer, otherwise raise a
        TypeError exception with the message size must be an integer.
        If size is less than 0, raise a ValueError exception with
        the message size must be >= 0.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a getter method to get the value of size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method to set the value of size.
        The value must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer.
        If value is less than 0, raise a ValueError exception with
        the message size must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This is a method that calculates and returns the current square area.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        This is a method that prints in stdout the square with the character #.
        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
