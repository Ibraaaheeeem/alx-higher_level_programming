#!/usr/bin/python3
"""This module defines the Square class"""


class Square:
    """Defines a  square
    Attributes:
        size (int): size of one side of the square
    """
    def __init__(self, size=0):
        """initializes the square instance
	with default to 0
        Args:
            size (int): size of one side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

