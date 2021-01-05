#!/usr/bin/python3
"""
Defining a square class
"""


class Square():
    """ square class
        Attributes:
            __size (int): the size of the square
            __position (tuple): the shift in position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ getter for position """
        return self.__position

    @position.setter
    def position(self, position):
        """ setter for position
            Args: position (tuple): the position of the square \
                based on the upper left corner
                                    """
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """ returns the area of Square"""
        return self.__size ** 2

    def my_print(self):
        """ print a size by size square using '#'s """
        if self.__size == 0:
            print("")
        else:
            for l in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                print(" " * self__position[0], end="")
                print("#" * self.__size)
