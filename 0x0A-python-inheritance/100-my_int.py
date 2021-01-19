#!/usr/bin/python3
""" Method that defines a class MyInt """


class MyInt(int):
    """ MyInt is a rebel.
        MyInt has == and != operators inverted """
    def __eq__(self, other):
        """ reverse the equal method """
        if self.__int__() == other.__int__():
            return False
        return True

    def __ne__(self, other):
        """ reverse the not equal method """
        if self.__int__() == other.__int__():
            return True
        return False
