from flask import request, jsonify
from models.schema.likeSchema import like_schema, likes_schema
from services import LikeService
from marshmallow import ValidationError
from utils.util import token_required, admin_required

@token_required
def add_like():
    try:
        like_data = like_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    new_like = LikeService.add_like(like_data)
    return jsonify({
        "message": "Like added successfully",
        "like": like_schema.dump(new_like)
    }), 201

@token_required
def remove_like(like_id):
    LikeService.remove_like(like_id)
    return jsonify({
        "message": "Like removed successfully"
    }), 200