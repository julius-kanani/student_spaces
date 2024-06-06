#!/usr/bin/env python3
"""Rooms API routes"""

from flask import jsonify, request, abort
from models import storage
from models.room import Room
from api.v1.views import app_views

@app_views.route('/rooms', methods=['GET'], strict_slashes=False)
def get_rooms():
    """Get all rooms"""
    rooms = storage.all('Room').values()
    return jsonify([room.to_dict() for room in rooms])

@app_views.route('/rooms/<room_id>', methods=['GET'], strict_slashes=False)
def get_room(room_id):
    """Get a specific room"""
    room = storage.get('Room', room_id)
    if not room:
        abort(404)
    return jsonify(room.to_dict())

@app_views.route('/rooms', methods=['POST'], strict_slashes=False)
def create_room():
    """Create a new room"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    if 'property_id' not in data or 'room_type' not in data or 'bed_count' not in data or 'monthly_rent' not in data:
        abort(400, "Missing fields")
    room = Room(**data)
    room.save()
    return jsonify(room.to_dict()), 201

@app_views.route('/rooms/<room_id>', methods=['PUT'], strict_slashes=False)
def update_room(room_id):
    """Update a room"""
    room = storage.get('Room', room_id)
    if not room:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(room, key, value)
    room.save()
    return jsonify(room.to_dict())

@app_views.route('/rooms/<room_id>', methods=['DELETE'], strict_slashes=False)
def delete_room(room_id):
    """Delete a room"""
    room = storage.get('Room', room_id)
    if not room:
        abort(404)
    room.delete()
    storage.save()
    return jsonify({}), 200
