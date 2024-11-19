from flask import request, jsonify
from models.schema.commentSchema import comment_schema, comments_schema
from services import CommentService
from marshmallow import ValidationError
from utils.util import token_required, admin_required

@token_required
def add_comment():
    try:
        comment_data = comment_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    new_comment = CommentService.add_comment(comment_data)
    return jsonify({
        "message": "Comment created successfully",
        "comment": comment_schema.dump(new_comment)
    }), 201

@admin_required
def get_all_comments():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_comments = CommentService.get_all_comments()
    return jsonify({
        "message": "All comments retrieved successfully",
        "comments": comments_schema.dump(all_comments, many=True)
    }), 200

@token_required
def get_comment_by_id(comment_id):
    comment = CommentService.get_comment_by_id(comment_id)
    return jsonify({
        "message": "Comment retrieved successfully",
        "comment": comment_schema.dump(comment)
    }), 200

@token_required
def get_comments_by_post_id(post_id):
    comments = CommentService.get_comments_by_post_id(post_id)
    return jsonify({
        "message": "Comments by post ID retrieved successfully",
        "comments": comments_schema.dump(comments)
    }), 200

@token_required
def get_comments_by_neighbor_id(neighbor_id):
    comments = CommentService.get_comments_by_neighbor_id(neighbor_id)
    return jsonify({
        "message": "Comments by neighbor ID retrieved successfully",
        "comments": comments_schema.dump(comments)
    }), 200

@token_required
def update_comment(comment_id):
    try:
        comment_data = comment_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    updated_comment = CommentService.update_comment(comment_id, comment_data)
    return jsonify({
        "message": "Comment updated successfully",
        "comment": comment_schema.dump(updated_comment)
    }), 200

@token_required
def delete_comment(comment_id):
    CommentService.delete_comment(comment_id)
    return jsonify({
        "message": "Comment deleted successfully"
    }), 200