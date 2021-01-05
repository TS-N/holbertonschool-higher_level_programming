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
        self.size = size

    @property
    def size(self):
        """ getter for size """
        return self.__size

    @size.setter
    def size(self, size):
        """ setter for size
            Args: size (int): the size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ returns the area of Square"""
        return self.__size ** 2
