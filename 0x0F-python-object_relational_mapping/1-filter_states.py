#!/usr/bin/python3
""" a script that lists all states
with a name starting with N (upper N) from the database """
import MySQLdb
import sys


def main():
    """ main function """

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states \
              WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rs = c.fetchall()
    for r in rs:
        print(r)
    c.close()
    db.close()


if __name__ == "__main__":
    main()
