#!/usr/bin/python3
"""And now the Square
    The square class tha inherits from Rectangle
    which inherits from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        s = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
        return s

    def update(self, *args, **kwargs):
        """ that assigns an argument to each attribute:
            1st arg should be the id attribute
            2nd arg should be the size attribute
            3th arg should be the x attribute
            4th arg should be the y attribute """
        if args is not None and args is not ():
            l = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, l[i], arg)
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        d = {}
        l = ['id', 'size', 'x', 'y']
        for e in l:
            d[e] = getattr(self, e)
        return d

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        super().update(self.id, value, value)
