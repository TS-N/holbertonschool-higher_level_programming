#!/usr/bin/python3
def add_attribute(obj, name, value):
    if '__dict__' in dir(obj):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
