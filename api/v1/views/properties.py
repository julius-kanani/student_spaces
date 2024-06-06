#!/usr/bin/env python3
"""Properties API routes"""

from flask import jsonify, request, abort
from models import storage
from models.property import Property
from api.v1.views import app_views

@app_views.route('/properties', methods=['GET'], strict_slashes=False)
def get_properties():
    """Get all properties"""
    properties = storage.all('Property').values()
    return jsonify([property.to_dict() for property in properties])

@app_views.route('/properties/<property_id>', methods=['GET'], strict_slashes=False)
def get_property(property_id):
    """Get a specific property"""
    property = storage.get('Property', property_id)
    if not property:
        abort(404)
    return jsonify(property.to_dict())

@app_views.route('/properties', methods=['POST'], strict_slashes=False)
def create_property():
    """Create a new property"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    if 'title' not in data or 'address' not in data or 'city' not in data or 'rent_price' not in data or 'landlord_id' not in data:
        abort(400, "Missing fields")
    property = Property(**data)
    property.save()
    return jsonify(property.to_dict()), 201

@app_views.route('/properties/<property_id>', methods=['PUT'], strict_slashes=False)
def update_property(property_id):
    """Update a property"""
    property = storage.get('Property', property_id)
    if not property:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(property, key, value)
    property.save()
    return jsonify(property.to_dict())

@app_views.route('/properties/<property_id>', methods=['DELETE'], strict_slashes=False)
def delete_property(property_id):
    """Delete a property"""
    property = storage.get('Property', property_id)
    if not property:
        abort(404)
    property.delete()
    storage.save()
    return jsonify({}), 200
