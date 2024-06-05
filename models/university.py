#!/usr/bin/env python3
"""The university module containing the University class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship

class University(BaseModel, Base):
    """Representation of a University."""
    __tablename__ = 'universities'

    name = Column(String(128), nullable=False)
    location = Column(String(256), nullable=False)
    abbreviation = Column(String(10), nullable=False)
    established_date = Column(Date, nullable=False)

    students = relationship("User", backref="university", cascade="all, delete-orphan")
