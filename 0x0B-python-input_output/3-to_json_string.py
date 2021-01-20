#!/usr/bin/python3
""" json encoding module """
import json


def to_json_string(my_obj):
    """ encode an object (string) to json format """
    return json.dumps(my_obj)
