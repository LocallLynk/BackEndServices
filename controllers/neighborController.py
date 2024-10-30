from flask import request, jsonify
from models.schemas.neighborSchema import neighbor_schema, neighbors_schema, neighbor_login
from models.schemas.skillSchema import skill_schema
from services import NeighborService
from models.neighbor import Neighbor
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required
from models.task import Task

def create_neighbor():
    try:
        neighbor_data = neighbor_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_neighbor = NeighborService.create_neighbor(neighbor_data)

    return neighbor_schema.jsonify(new_neighbor), 201

@cache.cached(timeout=50)
@admin_required
def get_all_neighbors():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = NeighborService.get_all_neighbors(page, per_page)

    return neighbors_schema.jsonify(all_neighbors), 200

def login():
    try:
        credentials = neighbor_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    token = NeighborService.login(credentials)

    if token:
        response = {
            "status": "success",
            "message": "successfully logging in",
            "token": token
        }
        return jsonify(response), 200
    else:
        return jsonify({"status": "error", "message": "invalid username or password"}), 404

@token_required
def get_neighbor_by_id(neighbor_id):
    return neighbor_schema.jsonify(neighbor_id), 200

@token_required
def update_neighbor(current_neighbor):
    try:
        neighbor_data = neighbor_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_neighbor = NeighborService.update_neighbor(current_neighbor, neighbor_data)

    return neighbor_schema.jsonify(updated_neighbor), 200

@token_required
def delete_neighbor(current_neighbor):
    NeighborService.delete_neighbor(current_neighbor)

    return '', 204

@token_required
def add_skill_to_neighbor(current_neighbor):
    try:
        skill_data = skill_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_skill = NeighborService.add_skill_to_neighbor(current_neighbor, skill_data)

    return skill_schema.jsonify(new_skill), 201

@token_required
def get_neighbor_by_skill(neighbor_skill):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = NeighborService.get_neighbor_by_skill(neighbor_skill, page, per_page)

    return neighbors_schema.jsonify(all_neighbors), 200

@token_required
def get_neighbor_by_task(task_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = NeighborService.get_neighbor_by_task(task_id, page, per_page)

    return neighbors_schema.jsonify(all_neighbors), 200

@token_required
def get_neighbor_by_feedback(feedback_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = NeighborService.get_neighbor_by_feedback(feedback_id, page, per_page)

    return neighbors_schema.jsonify(all_neighbors), 200

@token_required
def get_neighbor_by_rating(rating):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = NeighborService.get_neighbor_by_rating(rating, page, per_page)

    return neighbors_schema.jsonify(all_neighbors), 200

@token_required
def get_neighbor_by_username(username):
    return neighbor_schema.jsonify(username), 200

@token_required
def get_neighbor_by_email(email):
    return neighbor_schema.jsonify(email), 200

@token_required
def get_neighbor_by_zipcode(zipcode):
    return neighbors_schema.jsonify(zipcode), 200






