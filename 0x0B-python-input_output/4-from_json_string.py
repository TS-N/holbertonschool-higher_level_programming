#!/usr/bin/python3
""" json decoding module """
import json


def from_json_string(my_obj):
    """ decode a json string to python object """
    return json.loads(my_obj)
