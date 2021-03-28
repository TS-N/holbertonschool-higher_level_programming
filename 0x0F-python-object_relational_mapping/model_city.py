#!/usr/bin/python3
""" model for cities """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """ basic state class using SQLAlchemy """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False,  primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
