#!/usr/bin/env python3
"""Bookings API routes"""

from flask import jsonify, request, abort
from models import storage
from models.booking import Booking
from api.v1.views import app_views

@app_views.route('/bookings', methods=['GET'], strict_slashes=False)
def get_bookings():
    """Get all bookings"""
    bookings = storage.all('Booking').values()
    return jsonify([booking.to_dict() for booking in bookings])

@app_views.route('/bookings/<booking_id>', methods=['GET'], strict_slashes=False)
def get_booking(booking_id):
    """Get a specific booking"""
    booking = storage.get('Booking', booking_id)
    if not booking:
        abort(404)
    return jsonify(booking.to_dict())

@app_views.route('/bookings', methods=['POST'], strict_slashes=False)
def create_booking():
    """Create a new booking"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    if 'room_id' not in data or 'student_id' not in data or 'start_date' not in data or 'end_date' not in data:
        abort(400, "Missing fields")
    booking = Booking(**data)
    booking.save()
    return jsonify(booking.to_dict()), 201

@app_views.route('/bookings/<booking_id>', methods=['PUT'], strict_slashes=False)
def update_booking(booking_id):
    """Update a booking"""
    booking = storage.get('Booking', booking_id)
    if not booking:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(booking, key, value)
    booking.save()
    return jsonify(booking.to_dict())

@app_views.route('/bookings/<booking_id>', methods=['DELETE'], strict_slashes=False)
def delete_booking(booking_id):
    """Delete a booking"""
    booking = storage.get('Booking', booking_id)
    if not booking:
        abort(404)
    booking.delete()
    storage.save()
    return jsonify({}), 200
