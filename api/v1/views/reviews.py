#!/usr/bin/env python3
"""Reviews API routes"""

from flask import jsonify, request, abort
from models import storage
from models.review import Review
from api.v1.views import app_views

@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def get_reviews():
    """Get all reviews"""
    reviews = storage.all('Review').values()
    return jsonify([review.to_dict() for review in reviews])

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Get a specific review"""
    review = storage.get('Review', review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())

@app_views.route('/reviews', methods=['POST'], strict_slashes=False)
def create_review():
    """Create a new review"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    if 'property_id' not in data or 'user_id' not in data or 'rating' not in data or 'comment' not in data:
        abort(400, "Missing fields")
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201

@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update a review"""
    review = storage.get('Review', review_id)
    if not review:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.json
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict())

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Delete a review"""
    review = storage.get('Review', review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200
