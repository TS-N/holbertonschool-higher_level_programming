#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for l in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            if i != 0:
                print("")
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
        print("")
