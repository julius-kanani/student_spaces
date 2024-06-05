#!/usr/bin/env python3
"""The property module containing the Property class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Text, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

class Property(BaseModel, Base):
    """Representation of a Property."""
    __tablename__ = 'properties'

    landlord_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(128), nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String(256), nullable=False)
    city = Column(String(128), nullable=False)
    rent_price = Column(DECIMAL, nullable=False)
    is_available = Column(Boolean, default=True, nullable=False)

    rooms = relationship("Room", backref="property", cascade="all, delete-orphan")
    reviews = relationship("Review", backref="property", cascade="all, delete-orphan")
