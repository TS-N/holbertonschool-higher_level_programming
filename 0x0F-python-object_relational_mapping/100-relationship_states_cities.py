#!/usr/bin/python3
""" creates the State California with the City San Francisco
from the database hbtn_0e_100_usa """
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ci = City(name="San Fransisco", state=State(name="California"))
    session.add(ci)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
