#!/usr/bin/env python3
"""The user module containing the User class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Representation of a User."""
    __tablename__ = 'users'

    username = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    full_name = Column(String(128), nullable=True)
    phone_number = Column(String(20), nullable=True, unique=True)
    user_type = Column(Enum('student', 'landlord', name='user_types'), nullable=False)
    university_id = Column(Integer, ForeignKey('universities.id'), nullable=False)

    properties = relationship("Property", backref="landlord", cascade="all, delete-orphan")
    bookings = relationship("Booking", backref="student", cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
