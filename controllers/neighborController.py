from flask import request, jsonify
from models.schema.neighborSchema import neighbor_schema, neighbors_schema, neighbor_login
from models.schema.skillSchema import skill_schema
from services import NeighborService
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required


def create_neighbor():
    try:
        neighbor_data = neighbor_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_neighbor = NeighborService.create_neighbor(neighbor_data)

    return jsonify({
        "message": "Neighbor created successfully",
        "neighbor": neighbor_schema.dump(new_neighbor)
    }), 201

@cache.cached(timeout=50)
@admin_required
def get_all_neighbors():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = NeighborService.get_all_neighbors(page, per_page)

    return jsonify({
        "message": "Neighbors retrieved successfully",
        "neighbors": neighbors_schema.dump(all_neighbors, many=True)
    }), 200

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
    neighbor = NeighborService.get_neighbor_by_id(neighbor_id)
    return jsonify({
        "message": "Neighbor retrieved successfully",
        "neighbor": neighbor_schema.dump(neighbor)
    }), 200

@token_required
def update_neighbor(current_neighbor):
    try:
        neighbor_data = neighbor_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_neighbor = NeighborService.update_neighbor(current_neighbor, neighbor_data)

    return jsonify({
        "message": "Neighbor updated successfully",
        "neighbor": neighbor_schema.dump(updated_neighbor)
    }), 200

@token_required
def delete_neighbor(current_neighbor):
    NeighborService.delete_neighbor(current_neighbor)

    return jsonify({"message": "Neighbor deleted successfully"}), 204

@token_required
def add_skill_to_neighbor(current_neighbor):
    try:
        skill_data = skill_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_skill = NeighborService.add_skill_to_neighbor(current_neighbor, skill_data)

    return jsonify({
        "message": "Skill added to neighbor successfully",
        "skill": skill_schema.dump(new_skill)
    }), 201

@token_required
def get_neighbor_by_skill(neighbor_skill):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbors = NeighborService.get_neighbor_by_skill(neighbor_skill, page, per_page)

    return jsonify({
        "message": "Neighbors with skill retrieved successfully",
        "neighbors": neighbors_schema.dump(neighbors, many=True)
    }), 200

@token_required
def get_neighbor_by_task(task_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbors = NeighborService.get_neighbor_by_task(task_id, page, per_page)

    return jsonify({
        "message": "Neighbors by task retrieved successfully",
        "neighbors": neighbors_schema.dump(neighbors, many=True)
    }), 200

@token_required
def get_neighbor_by_feedback(feedback_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbors = NeighborService.get_neighbor_by_feedback(feedback_id, page, per_page)

    return jsonify({
        "message": "Neighbors by feedback retrieved successfully",
        "neighbors": neighbors_schema.dump(neighbors, many=True)
    }), 200

@token_required
def get_neighbor_by_rating(rating):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbors = NeighborService.get_neighbor_by_rating(rating, page, per_page)

    return jsonify({
        "message": "Neighbors by rating retrieved successfully",
        "neighbors": neighbors_schema.dump(neighbors, many=True)
    }), 200

@token_required
def get_neighbor_by_username(username):
    neighbor = NeighborService.get_neighbor_by_username(username)
    return jsonify({
        "message": "Neighbor by username retrieved successfully",
        "neighbor": neighbor_schema.dump(neighbor)
    }), 200

@token_required
def get_neighbor_by_email(email):
    neighbor = NeighborService.get_neighbor_by_email(email)
    return jsonify({
        "message": "Neighbor by email retrieved successfully",
        "neighbor": neighbor_schema.dump(neighbor)
    }), 200

@token_required
def get_neighbor_by_zipcode(zipcode):
    neighbors = NeighborService.get_neighbor_by_zipcode(zipcode)
    return jsonify({
        "message": "Neighbors by zipcode retrieved successfully",
        "neighbors": neighbors_schema.dump(neighbors, many=True)
    }), 200






