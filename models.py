from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base() 

class Chest(Base):
    __tablename__ = 'chest'
    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)

class Back(Base):
    __tablename__ = 'back'
    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    
class Arms(Base):
    __tablename__ = 'arms'
    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    arm_subgroup = Column(String)
    
class Legs(Base):
    __tablename__ = 'legs'
    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)

engine = create_engine('sqlite:///./data/exercises.sqlite')

session = sessionmaker()
session.configure(bind=engine)