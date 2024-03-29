#!/usr/bin/python3
"""a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb


def main():
    """ main function """

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states \
               WHERE name = BINARY '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    rs = c.fetchall()
    for r in rs:
        print(r)
    c.close()
    db.close()


if __name__ == "__main__":
    main()
