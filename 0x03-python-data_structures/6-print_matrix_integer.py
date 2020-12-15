#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        sp = ""
        for i, n in enumerate(row):
            if i != 0:
                sp = " "
            print("{}{:d}".format(sp, n), end="")
        print()
