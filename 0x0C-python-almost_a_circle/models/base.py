#!/usr/bin/python3
""" 1. Base class """
import json


class Base:
    """ manage id attribute in all your future classes """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionary):
        """ that returns the JSON string representation of list_dictionaries """
        if list_dictionary is None or list_dictionary == []:
            return "[]"
        return json.dumps(list_dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = str(cls.__name__) + ".json"
        l =
        with open(filename, "w") as f:
                s = Base.to_json_string(list_objs)
                print(s)

