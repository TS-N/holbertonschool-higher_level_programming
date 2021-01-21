#!/usr/bin/python3
""" Method that defines a class Student """


class Student:
    """ A basic student class """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retreives a dict of all the class attributes """
        al = self.__dict__
        if attrs is None:
            return al
        dic = {}
        for attr in attrs:
            if attr in al:
                dic[attr] = al[attr]
        return dic
