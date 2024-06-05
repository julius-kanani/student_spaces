#!/usr/bin/env python3
"""The review module containing the Review class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey

class Review(BaseModel, Base):
    """Representation of a Review."""
    __tablename__ = 'reviews'

    property_id = Column(String(60), ForeignKey('properties.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)
