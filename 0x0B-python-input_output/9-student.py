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

    def to_json(self):
        """ retreives a dict of all the class attributes """
        return self.__dict__
