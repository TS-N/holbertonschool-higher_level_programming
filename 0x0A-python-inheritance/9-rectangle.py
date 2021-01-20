#!/usr/bin/python3
""" a Base class for geometry shapes"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a Rectangle shape based of BaseGeometry class """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ computes the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(
                self.__width,
                self.__height)

