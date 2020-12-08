#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        a = 0
    else:
        a = -32
    print(chr(i + a), end='')
