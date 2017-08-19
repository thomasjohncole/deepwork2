import sys

from sqlalchemy import Column, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# creates a table with the specified columns #
class Dailyhours(Base):
    __tablename__ = 'dailyhours'

    work_date = Column(Date, primary_key = True)
    day = Column(String(10))
    hours_worked = Column(Float)
    remarks = Column(String(250))

# creates the database #
engine = create_engine( 'sqlite:///deepwork.db')

Base.metadata.create_all(engine)

