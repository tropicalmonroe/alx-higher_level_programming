#!/usr/bin/python3
"""Defines Rectangle class"""


class Rectangle:
    """Represent a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances
        print_symbol (any): The symbol used for string representation
    """
    numbinst = 0
    printsymb = "#"

    def __init__(self, width=0, height=0):
        """Init a new Rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        type(self).numbinst += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns getter/setter width of rec"""
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
        """Getter/setter the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the representation of the Rectangle with # symbol"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append(str(self.printsymb)) for j in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns str representation of the Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).numbinst -= 1
        print("Bye rectangle...")
