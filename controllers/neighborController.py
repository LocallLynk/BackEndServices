from flask import request, jsonify
from models.schema.neighborSchema import neighbor_schema, neighbors_schema, neighbor_login, neighborz_schema
from services import NeighborService
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required, get_current_user


def create_neighbor():
    try:
        neighbor_data = neighbor_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_neighbor = NeighborService.create_neighbor(neighbor_data)

    return jsonify({
        "message": "Neighbor created successfully",
        "neighbor": neighborz_schema.dump(new_neighbor)
       
    }), 201

@token_required
def home_feed():
    
    user_id = request.current_user  
    feed_data = NeighborService.get_home_feed(user_id)

    return jsonify(feed_data), 200

# @cache.cached(timeout=50)
#@admin_required
def get_all_neighbors():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

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
    
@admin_required
def remove_admin(neighbor_id):
    neighbor = NeighborService.remove_admin(neighbor_id)

    if neighbor:
        return jsonify({
            "message": "Neighbor is no longer an admin",
            
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
    
def validate_user():
    try:
        user_data = user_validation.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    user = NeighborService.validate_user(user_data)
    if user:
        return jsonify({
            "message": "User validated successfully",
            "user": neighborz_schema.dump(user)
        }), 200
    else:
        return jsonify({"message": "User not found, sending to create neighbor"}), 404
    
#@token_required
def get_neighbor_by_id(neighbor_id):
    neighbor = NeighborService.get_neighbor_by_id(neighbor_id)
    if not neighbor:
        return jsonify({"message": "Neighbor not found"}), 404

    return jsonify({
        "message": "Neighbor retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)

        
    }), 200

@token_required
def update_neighbor(neighbor_id):
    try:
        neighbor_data = neighbor_schema.load(request.json)
        # if neighbor_id != get_current_user():
        #     return jsonify({"message": "Unauthorized"}), 403
    except ValidationError as e:
        return jsonify(e.messages), 400
    if not neighbor_id:
        return jsonify({"message": "Neighbor not found"}), 404

    NeighborService.update_neighbor(neighbor_id, neighbor_data)

    return jsonify({
        "message": "Neighbor updated successfully"
        
    }), 200

@token_required
def delete_neighbor(neighbor_id):
    if not neighbor_id:
        return jsonify({"message": "Neighbor not found"}), 404
    # if neighbor_id != get_current_user():
    #     return jsonify({"message": "Unauthorized"}), 403
    NeighborService.delete_neighbor(neighbor_id)

    return jsonify({"message": "Neighbor deleted successfully"}), 204


#@token_required
def get_neighbor_by_username(username):
    neighbor = NeighborService.get_neighbor_by_username(username)
    return jsonify({
        "message": "Neighbor by username retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
    }), 200

#@token_required
def get_neighbor_by_email(email):
    neighbor = NeighborService.get_neighbor_by_email(email)
    return jsonify({
        "message": "Neighbor by email retrieved successfully",
        "neighbor": neighborz_schema.dump(neighbor)
    }), 200

#@token_required
def get_neighbor_by_zipcode(zipcode):
    neighbor = NeighborService.get_neighbor_by_zipcode(zipcode)
    return jsonify({
        "message": "Neighbors by zipcode retrieved successfully",
        "neighbor": neighbors_schema.dump(neighbor)
    }), 200






