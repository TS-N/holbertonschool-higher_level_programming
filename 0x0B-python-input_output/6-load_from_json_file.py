#!/usr/bin/python3
"""module for a method that load from a json file """
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as f:
        s = json.load(f)
    return s
