from flask import request, jsonify
from models.schema.shareSchema import share_schema, shares_schema
from services import ShareService
from marshmallow import ValidationError
from utils.util import token_required, admin_required

@token_required
def add_share():
    try:
        share_data = share_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    new_share = ShareService.add_share(share_data)
    return jsonify({
        "message": "Share added successfully",
        "share": share_schema.dump(new_share)
    }), 201

@token_required
def remove_share(share_id):
    ShareService.remove_share(share_id)
    return jsonify({
        "message": "Share removed successfully"
    }), 200

@token_required
def get_share_by_id(share_id):
    share = ShareService.get_share_by_id(share_id)
    return jsonify({
        "message": "Share retrieved successfully",
        "share": share_schema.dump(share)
    }), 200

@admin_required
def get_all_shares():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_shares = ShareService.get_all_shares()
    return jsonify({
        "message": "All shares retrieved successfully",
        "shares": shares_schema.dump(all_shares, many=True)
    }), 200

@token_required
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