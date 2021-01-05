#!/usr/bin/python3
"""
Defining a square class
"""


class Square():
    """ square class
        Attributes:
            __size (int): the size of the square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the area of Square"""
        return self.__size ** 2
