from flask import request, jsonify
from models.schema.dislikeSchema import dislike_schema, dislikes_schema
from services import DislikeService
from marshmallow import ValidationError
from utils.util import token_required, admin_required, get_current_user

@token_required
def add_dislike():
    neighbor_id = get_current_user()
    request.json['neighbor_id'] = neighbor_id
    try:
        dislike_data = dislike_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    new_dislike = DislikeService.add_dislike(dislike_data)
    return jsonify({
        "message": "Dislike added successfully",
        "dislike": dislike_schema.dump(new_dislike)
    }), 201

@token_required
def remove_dislike(dislike_id):
    DislikeService.remove_dislike(dislike_id)
    return jsonify({
        "message": "Dislike removed successfully"
    }), 200