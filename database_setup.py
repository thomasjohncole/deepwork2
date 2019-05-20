import sys

from sqlalchemy import Column, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session # new and below
# http://flask.pocoo.org/docs/dev/patterns/sqlalchemy/

engine = create_engine( 'sqlite:///deepwork.db') # moved this up from the bottom
DBSession = scoped_session(sessionmaker(bind=engine)) # new 05/2019
Base = declarative_base()
Base.query = DBSession.query_property()
# new 05/2019 this allows Unique class code to function properly

# creates a table with the specified columns #
class Dailyhours(Base):
    __tablename__ = 'dailyhours'

    work_date = Column(Date, primary_key = True)
    hours_worked = Column(Float)
    remarks = Column(String(250))

#This does the schema generation
Base.metadata.create_all(engine)
