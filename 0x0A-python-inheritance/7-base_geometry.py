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
