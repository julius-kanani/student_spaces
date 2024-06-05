#!/usr/bin/env python3
"""The db_storage module that contains the DBStorage class."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from os import getenv

class DBStorage:
    """Interacts with the MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = getenv("SS_MYSQL_USER")
        passwd = getenv("SS_MYSQL_PWD")
        host = getenv("SS_MYSQL_HOST")
        db = getenv("SS_MYSQL_DB")
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}', pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session"""
        objects = {}
        if cls:
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                objects[key] = obj
        else:
            for clss in models.classes.values():
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        from models.base_model import Base
        from models.user import User
        from models.property import Property
        from models.room import Room
        from models.booking import Booking
        from models.review import Review
        from models.university import University

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.remove()
