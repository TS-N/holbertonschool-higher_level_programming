#!/usr/bin/python3
""" deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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
    objs = session.query(State).filter(State.name.like('%a%')).all()
    for obj in objs:
        session.delete(obj)
    session.commit()


if __name__ == "__main__":
    main()
