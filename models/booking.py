#!/usr/bin/env python3
"""The booking module containing the Booking class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey

class Booking(BaseModel, Base):
    """Representation of a Booking."""
    __tablename__ = 'bookings'

    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(Enum('pending', 'confirmed', 'canceled', name='booking_statuses'), nullable=False)
