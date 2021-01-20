#!/usr/bin/python3
""" 15. Hack the VM """
import sys
import os


def main():
    """ finds a string in the heap of a running process, and replaces it """
    if len(sys.argv) != 4:
        print("usage: read_write_heap.py pid search_string replace_string")
        return 1
    pid = sys.argv[1]
    old_string = sys.argv[2]
    new_string = sys.argv[3]
    pad = len(old_string) - len(new_string)
    if pad < 0:
        pad = 0

    with open("/proc/" + pid + "/maps", mode="r") as maps:
        lines = maps.readlines()
    for line in lines:
        sp = line.split()
        if '[heap]' in sp:
            break
    addresses = sp[0].split('-')
    start_add = int(addresses[0], 16)
    end_add = int(addresses[1], 16)
    with open("/proc/" + pid + "/mem", mode="rb+") as mem:
        mem.seek(start_add)
        rel_add = 0
        while (rel_add <= 30):
            try:
                s = mem.read(len(old_string))
                mem.seek(start_add + rel_add, 0)
                if s == bytes(old_string, 'ascii'):
                    mem.write(bytes(new_string, 'ascii'))
                    for i in range(0, pad):
                        mem.write(bytes('\0', 'ascii'))
                    break
            except Exception as e:
                print(e)
                pass
            mem.seek(1, 1)
            rel_add += 1
    return 0

if __name__ == "__main__":
    main()
