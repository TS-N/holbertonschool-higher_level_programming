#!/usr/bin/python3
import sys
l = len(sys.argv)
if l == 1:
    s = "s."
elif l == 2:
    s =":"
else:
    s = "s:"
print("{:d} argument{}".format(l - 1, s))
for i in range(1, l):
    print("{}: {}".format(i, sys.argv[i]))
