from flask import request, jsonify
from models.schema.shareSchema import share_schema, shares_schema
from services import ShareService
from marshmallow import ValidationError
from utils.util import token_required, admin_required, get_current_user
from models.shares import Share

#@token_required
def add_share():
    neighbor_id = get_current_user()
    request.json['neighbor_id'] = neighbor_id  # Add neighbor ID to the request data
    
    try:
        # Validate and load data into a dictionary
        share_data = share_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    
    # Create a new Share instance explicitly
    new_share = Share(**share_data)

    try:
        # Call the service to add the share
        added_share = ShareService.add_share(new_share)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "message": "Share added successfully",
        "share": share_schema.dump(added_share)
    }), 201


#@token_required
def remove_share(share_id):
    ShareService.remove_share(share_id)
    return jsonify({
        "message": "Share removed successfully"
    }), 200

#@token_required
def get_share_by_id(share_id):
    share = ShareService.get_share_by_id(share_id)
    return jsonify({
        "message": "Share retrieved successfully",
        "share": share_schema.dump(share)
    }), 200

#@token_required
def update_share(share_id):
    try:
        share_data = share_schema.load(request.json)
        
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    updated_share = ShareService.update_share(share_id, share_data)
    return jsonify({
        "message": "Share updated successfully",
        "share": share_schema.dump(updated_share)
    }), 200