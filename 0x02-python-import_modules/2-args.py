#!/usr/bin/python3
import sys
l = len(sys.argv)
print("{:d} argument{}".format(l - 1, "." if l == 1 else ":"))
for i in range(1, l):
    print("{}: {}".format(i, sys.argv[i]))
