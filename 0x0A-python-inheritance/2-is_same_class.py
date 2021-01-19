#!/usr/bin/python3
""" is same class fucntion """


def is_same_class(obj, a_class):
    """ returns True if the object is
        exactly an instance of the specified class
        otherwise False """
    if obj.__class__ is a_class:
        return True
    return False
