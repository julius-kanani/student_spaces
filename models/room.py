#!/usr/bin/env python3
"""The room module containing the Room class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

class Room(BaseModel, Base):
    """Representation of a Room."""
    __tablename__ = 'rooms'

    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)
    room_type = Column(String(128), nullable=False)
    bed_count = Column(Integer, nullable=False)
    monthly_rent = Column(DECIMAL, nullable=False)
    is_available = Column(Boolean, default=True, nullable=False)

    bookings = relationship("Booking", backref="room", cascade="all, delete-orphan")
