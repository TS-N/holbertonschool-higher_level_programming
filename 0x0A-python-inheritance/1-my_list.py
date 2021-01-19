#!/usr/bin/python3
""" An example of class based on list """


class MyList(list):
    """ my list class """
    def print_sorted(self):
        """ that prints the list,
            but sorted (ascending sort) """
        print(sorted(super().copy()))
