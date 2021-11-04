import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__='characters'
    idCharact = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    haircolor = Column(String(250))
    eyecolor = Column(String(250))

class Planets(Base):
    __tablename__='planets'
    idPlanet = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer)
    orbitalPeriod = Column(Integer)
    rotationPeriod = Column(Integer)
    diameter = Column(Integer)

class Users(Base):
    __tablename__='users'
    userId = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(150))
    username = Column(String(250))
    password = Column(String(150))

class Favorites(Base):
    __tablename__='favorites'
    favId = Column(Integer, primary_key=True)
    idCharact = Column(Integer, ForeignKey('characters.idCharact'))
    idPlanet = Column(Integer, ForeignKey('planets.idPlanet'))
    userId = Column(Integer, ForeignKey('users.userId'))
    characters = relationship(Characters)
    planets = relationship(Planets)
    users = relationship(Users)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')