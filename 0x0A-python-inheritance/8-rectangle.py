#!/usr/bin/python3
""" a Base class for geometry shapes"""


class BaseGeometry():
    """a basic base class"""
    def area(self):
        """ a function that gives the area of the shape """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the given parameter"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ a Rectangle shape based of BaseGeometry class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("hight", height)
        self.__height = height
