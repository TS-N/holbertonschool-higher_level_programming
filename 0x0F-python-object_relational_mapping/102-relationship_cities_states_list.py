#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base


def main():
    """main function """

    dialect = 'mysql'
    driver = 'mysqldb'
    username = sys.argv[1]
    password = sys.argv[2]
    host = 'localhost'
    port = '3306'
    database = sys.argv[3]
    engine = create_engine("{}+{}://{}:{}@{}:{}/{}".format(dialect,
                                                           driver,
                                                           username,
                                                           password,
                                                           host,
                                                           port,
                                                           database))
    Session = sessionmaker(bind=engine)
    session = Session()
    rs = session.query(City.id, City.name, State.name)\
        .join(State, City.state_id == State.id, isouter=True).all()
    for r in rs:
        print("{}: {} -> {}".format(r[0], r[1], r[2]))


if __name__ == "__main__":
    main()
