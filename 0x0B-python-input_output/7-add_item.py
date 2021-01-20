#!/usr/bin/python3
""" 7. Load, add, save  """
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """ script that adds all arguments to a Python list,
    and then save them to a file """
    filename = "add_item.json"
    l = sys.argv[1:]
    with open(filename, mode='a', encoding="utf-8") as f:
        pass
    try:
        l += load_from_json_file(filename)
    except:
        pass
    save_to_json_file(l, filename)

if __name__ == "__main__":
    main()
