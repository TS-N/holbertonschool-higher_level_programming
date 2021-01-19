#!/usr/bin/python3
""" some content to please the checker """


def add_attribute(obj, name, value):
    """ adds a attribute if possible """
    if '__dict__' in dir(obj):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
