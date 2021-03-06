#!/usr/bin/python3
""" 2. First Rectangle
    Rectangle class inherited from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle that inherits from Base
            Attributes:
                __width : the width of the rectangle
                __height : the height of the rectangle
                __x : the horizontal shift of the rectangle
                __y : the vertical shift of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ computes the area of the reactangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        h = self.__height
        s = '\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') * h
        print(s, end="")

    def update(self, *args, **kwargs):
        """ that assigns an argument to each attribute:
            1st arg should be the id attribute
            2nd arg should be the width attribute
            3rd arg should be the height attribute
            4th arg should be the x attribute
            5th arg should be the y attribute """
        if args is not None and args is not ():
            l = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, l[i], arg)
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        d = {}
        l = ['id', 'width', 'height', 'x', 'y']
        for e in l:
            d[e] = getattr(self, e)
        return d

    def __str__(self):
        """ replace the __str__ method """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
