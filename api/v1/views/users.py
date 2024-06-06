#!/usr/bin/env python3
"""Users API routes"""

from flask import jsonify, request, abort
from models import storage
from models.user import User
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Get all users"""
    users = storage.all("User").values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get a specific user"""
    user = storage.get('User', user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new user"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    if 'username' not in data or 'password' not in data or 'email' not in data:
        abort(400, "Missing fields")
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update a user"""
    user = storage.get('User', user_id)
    if not user:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user"""
    user = storage.get('User', user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200
