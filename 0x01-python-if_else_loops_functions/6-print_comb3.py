#!/usr/bin/python3
for d in range(0, 9):
    for u in range(d, 10):
        if d == 8 and u == 9:
            print("{}{}".format(d, u))
        else:
            if d != u:
                print("{}{}".format(d, u), end=", ")
