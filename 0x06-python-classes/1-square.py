#!/usr/bin/python3
"""
This module contains the Square class which defines a square
and adds a private instance.
"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
