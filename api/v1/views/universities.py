#!/usr/bin/env python3
"""Universities API routes"""

from flask import jsonify, request, abort
from models import storage
from models.university import University
from api.v1.views import app_views

@app_views.route('/universities', methods=['GET'], strict_slashes=False)
def get_universities():
    """Get all universities"""
    universities = storage.all('University').values()
    return jsonify([university.to_dict() for university in universities])

@app_views.route('/universities/<university_id>', methods=['GET'], strict_slashes=False)
def get_university(university_id):
    """Get a specific university"""
    university = storage.get('University', university_id)
    if not university:
        abort(404)
    return jsonify(university.to_dict())

@app_views.route('/universities', methods=['POST'], strict_slashes=False)
def create_university():
    """Create a new university"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    if 'name' not in data or 'location' not in data or 'abbreviation' not in data or 'established_date' not in data:
        abort(400, "Missing fields")
    university = University(**data)
    university.save()
    return jsonify(university.to_dict()), 201

@app_views.route('/universities/<university_id>', methods=['PUT'], strict_slashes=False)
def update_university(university_id):
    """Update a university"""
    university = storage.get('University', university_id)
    if not university:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(university, key, value)
    university.save()
    return jsonify(university.to_dict())

@app_views.route('/universities/<university_id>', methods=['DELETE'], strict_slashes=False)
def delete_university(university_id):
    """Delete a university"""
    university = storage.get('University', university_id)
    if not university:
        abort(404)
    university.delete()
    storage.save()
    return jsonify({}), 200
