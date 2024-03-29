#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rep a square"""

    def __init__(self, size):
        """Init a new square
        Args:
            size (int): The size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
