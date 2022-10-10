#!/usr/bin/python3
""" states cities containing the class city """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """ contains the class defination of city """
    __tablename__ = 'cities'

    id = Column(Integer, primarykey=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
