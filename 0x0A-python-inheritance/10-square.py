#!/usr/bin/python3
""" a Base class for geometry shapes"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ an class for squares """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ computes the area for a square """
        return self.__size ** 2
