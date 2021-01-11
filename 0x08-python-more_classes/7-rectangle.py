#!/usr/bin/python3
"""
Defining a rectangle class
"""


class Rectangle:
    """ Rectangle class
        Attributes:
                __width: the width of the rectangle
                __height: the height of the rectangle
                number_of_instances
                print_symbol
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        s = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(0, self.__height):
                if i != 0:
                    s += '\n'
                s += str(self.print_symbol) * self.__width
        return s

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ return the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
