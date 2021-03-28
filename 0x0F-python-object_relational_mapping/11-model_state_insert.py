#!/usr/bin/python3
"""adds the State object Louisiana to the database hbtn_0e_6_usa"""
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
    new_entry = State(id=None, name='Louisiana')
    session.add(new_entry)
    session.commit()
    print(new_entry.id)


if __name__ == "__main__":
    main()
