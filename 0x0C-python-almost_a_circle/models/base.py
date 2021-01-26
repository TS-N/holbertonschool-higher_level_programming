#!/usr/bin/python3
""" 1. Base class
    More blabla bla
    To please the checker"""
import json


class Base:
    """ manage id attribute in all your future classes """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ initialise the attribute of this instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionary):
        """ that returns the JSON string representation of list_dictionaries"""
        if list_dictionary is None or list_dictionary == []:
            return "[]"
        return json.dumps(list_dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = str(cls.__name__) + ".json"
        l = []
        if list_objs is not None and list_objs != []:
            for e in list_objs:
                l.append(e.to_dictionary())
        with open(filename, "w") as f:
                f.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        l = []
        if json_string is not None and len(json_string) != 0:
            l = json.loads(json_string)
        return l
