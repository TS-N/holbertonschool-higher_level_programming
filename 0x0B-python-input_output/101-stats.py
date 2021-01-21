#!/usr/bin/python3
""" 14. Log parsing """
import sys


def main():
    """ reads stdin line by line and computes metrics """
    code_status = {
                    '200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0
                    }
    tot_size = 0
    try:
        for i, line in enumerate(sys.stdin):
            info = line.rstrip('\n').split(' ')
            size = int(info[8])
            code = info[7]
            tot_size += size
            code_status[code] += 1
            if (i + 1) % 10 == 0:
                print("File size: {}".format(tot_size))
                for c in sorted(code_status):
                    if code_status[c] != 0:
                        print("{}: {}".format(c, code_status[c]))
    except KeyboardInterrupt as e:
        print("File size: {}".format(tot_size))
        for c in sorted(code_status):
            if code_status[c] != 0:
                print("{}: {}".format(c, code_status[c]))
        print(e)


if __name__ == "__main__":
    main()
