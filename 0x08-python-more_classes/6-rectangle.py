#!/usr/bin/python3
"""this is class rectangle"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        number_of_instances (int):
    """

    numinst = 0

    def __init__(self, width=0, height=0):
        """Init a new Rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        type(self).numinst += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height *2))

    def __str__(self):
        """Returns printable rep of the rectangle with # char """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the str representation of the Rect"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    ef __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).numbinst -= 1
        print("Bye rectangle...")
