#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa  """
import MySQLdb
import sys


def main():
    """ main function """

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name \
               FROM cities LEFT JOIN states ON cities.state_id = states.id")
    rs = c.fetchall()
    for r in rs:
        print(r)
    c.close()
    db.close()


if __name__ == "__main__":
    main()
