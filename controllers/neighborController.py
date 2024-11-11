from flask import request, jsonify
from models.schema.neighborSchema import neighbor_schema, neighbors_schema, neighbor_login, neighborz_schema
from models.schema.skillSchema import skill_schema, skills_schema
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
        "message": "Neighbor created successfully"
       
    }), 201

@cache.cached(timeout=50)
@admin_required
def get_all_neighbors():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = NeighborService.get_all_neighbors(page, per_page)

    return jsonify({
        "message": "Neighbors retrieved successfully",
        "data": neighbors_schema.dump(all_neighbors)
        
    }), 200

@admin_required
def make_admin(neighbor_id):
    neighbor = NeighborService.make_admin(neighbor_id)

    if neighbor:
        return jsonify({
            "message": "Neighbor is now an admin",
            
        }), 200
    else:
        return jsonify({"message": "Neighbor not found"}), 404
    
def login():
    try:
        
        credentials = neighbor_login.load(request.json)

    except ValidationError as e:
        
        return jsonify({"status": "error", "message": "Invalid input", "errors": e.messages}), 400

    token = NeighborService.login(credentials)

    if token:
        # Successful login response
        response = {
            "status": "success",
            "message": "Successfully logged in",
            "token": token
        }
        return jsonify(response), 200
    else:
        # Error response for invalid credentials
        return jsonify({"status": "error", "message": "Invalid username or password"}), 401
    
@token_required
def get_neighbor_by_id(neighbor_id):
    neighbor = NeighborService.get_neighbor_by_id(neighbor_id)

    return jsonify({
        "message": "Neighbor retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)

        
    }), 200

@token_required
def update_neighbor(current_neighbor):
    try:
        neighbor_data = neighbor_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    NeighborService.update_neighbor(current_neighbor, neighbor_data)

    return jsonify({
        "message": "Neighbor updated successfully"
        
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

    NeighborService.add_skill_to_neighbor(current_neighbor, skill_data)

    return jsonify({
        "message": "Skill added to neighbor successfully"
        
    }), 201

@token_required
def get_neighbor_by_skill(neighbor_skill):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbor = NeighborService.get_neighbor_by_skill(neighbor_skill, page, per_page)

    return jsonify({
        "message": "Neighbors with skill retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
        
    }), 200

@token_required
def get_neighbor_by_task(task_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbor = NeighborService.get_neighbor_by_task(task_id, page, per_page)

    return jsonify({
        "message": "Neighbors by task retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
        
    }), 200

@token_required
def get_neighbor_by_feedback(feedback_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbor = NeighborService.get_neighbor_by_feedback(feedback_id, page, per_page)

    return jsonify({
        "message": "Neighbors by feedback retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
    }), 200

@token_required
def get_neighbor_by_rating(rating):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    neighbor = NeighborService.get_neighbor_by_rating(rating, page, per_page)

    return jsonify({
        "message": "Neighbors by rating retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
    }), 200

@token_required
def get_neighbor_by_username(username):
    neighbor = NeighborService.get_neighbor_by_username(username)
    return jsonify({
        "message": "Neighbor by username retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
    }), 200

@token_required
def get_neighbor_by_email(email):
    neighbor = NeighborService.get_neighbor_by_email(email)
    return jsonify({
        "message": "Neighbor by email retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
    }), 200

@token_required
def get_neighbor_by_zipcode(zipcode):
    neighbor = NeighborService.get_neighbor_by_zipcode(zipcode)
    return jsonify({
        "message": "Neighbors by zipcode retrieved successfully",
        "neighbor": neighbors_schema.dump(neighbor)
    }), 200






