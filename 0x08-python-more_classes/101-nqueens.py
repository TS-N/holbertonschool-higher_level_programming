#!/usr/bin/python3
import sys
"""
A program that solves all possible N-queens problem solutions
"""


def indiag(la, li):
    """ checks if a queen is in the diagonal of another """
    ydiff = li[0] - la[0]
    if li[1] == la[1] + ydiff or li[1] == la[1] - ydiff:
        return True
    else:
        return False


def conflict(l, i):
    """ checks if a queen is conflicting with another """
    x = l[i][1]
    for a in range(0, i):
        if l[a][1] == x or indiag(l[a], l[i]) is True:
            return True
    return False


def place(l, i, N):
    """ recursive backtracking function that solves Nqueen problem """
    if i >= N:
        return True
    if i < 0:
        return False
    l[i][1] += 1
    if l[i][1] >= N:
        l[i][1] = -1
        return place(l, i - 1, N)
    else:
        if conflict(l, i) is True:
            return place(l, i, N)
        else:
            return place(l, i + 1, N)


def solve(N):
    """ gives all solution to a Nqueen solution """
    l = list([i, -1] for i in range(0, N))
    while place(l, 0, N) is True:
        print("{}".format(l))
        x0 = l[0][1]
        l = list([i, -1] for i in range(0, N))
        l[0][1] = x0


def main():
    """ main function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(N)

main()
