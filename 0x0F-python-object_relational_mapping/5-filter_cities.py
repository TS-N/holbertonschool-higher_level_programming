#!/usr/bin/python3
import MySQLdb
import sys
"""cript that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""


def main():
    """ main function """

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities \
               LEFT JOIN states ON cities.state_id = states.id \
               WHERE states.name = %s",
              (sys.argv[4],))
    rs = c.fetchall()
    l = [col for r in rs for col in r]
    print(", ".join(l))

    c.close()
    db.close()


if __name__ == "__main__":
    main()
