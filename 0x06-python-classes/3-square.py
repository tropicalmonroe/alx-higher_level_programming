#!/usr/bin/python3
"""Define a class Squar"""


class Square:
    """Represent a sq"""

    def __init__(self, size=0):
        """Initialize a new Squar

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""

        return (self.__size * self.__size)
