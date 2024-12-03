from flask import request, jsonify
from models.schema.commentSchema import comment_schema, comments_schema
from services import CommentService
from marshmallow import ValidationError
from utils.util import token_required, admin_required, get_current_user
from models.comment import Comment
from database import db

@token_required
def add_comment():
    neighbor_id = get_current_user()
    request.json['neighbor_id'] = neighbor_id
    try:
        # Validate and deserialize JSON input
        comment_data = comment_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    # Create a Comment instance from the validated data
    new_comment = Comment(**comment_data)

    # Pass the Comment instance to the service
    added_comment = CommentService.add_comment(new_comment)

    return jsonify({
        "message": "Comment created successfully",
        "comment": comment_schema.dump(added_comment)
    }), 201


#@admin_required
def get_all_comments():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_comments = CommentService.get_all_comments()
    return jsonify({
        "message": "All comments retrieved successfully",
        "comments": comments_schema.dump(all_comments, many=True)
    }), 200

#@token_required
def get_comment_by_id(comment_id):
    comment = CommentService.get_comment_by_id(comment_id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404
    return jsonify({
        "message": "Comment retrieved successfully",
        "comment": comment_schema.dump(comment)
    }), 200

#@token_required
def get_comments_by_post_id(post_id):
    comments = CommentService.get_comments_by_post_id(post_id)
    if not comments:
        return jsonify({"error": "No comments found for post"}), 404
    return jsonify({
        "message": "Comments by post ID retrieved successfully",
        "comments": comments_schema.dump(comments)
    }), 200

#@token_required
def get_comments_by_neighbor_id(neighbor_id):
    comments = CommentService.get_comments_by_neighbor_id(neighbor_id)
    if not comments:
        return jsonify({"error": "No comments found for neighbor"}), 404
    return jsonify({
        "message": "Comments by neighbor ID retrieved successfully",
        "comments": comments_schema.dump(comments)
    }), 200

#@token_required
def update_comment(comment_id):
    # Get the current user from the token
    neighbor_id = get_current_user()

    # Fetch the comment from the database
    comment = db.session.get(Comment, comment_id)

    # Check if the comment exists
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    # Validate the input data
    try:
        comment_data = comment_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    # Update the comment
    updated_comment = CommentService.update_comment(comment_id, comment_data)

    return jsonify({
        "message": "Comment updated successfully",
        "comment": comment_schema.dump(updated_comment)
    }), 200


#@token_required
def delete_comment(comment_id):
    # Get the current user from the token
    neighbor_id = get_current_user()

    # Fetch the comment from the database
    comment = db.session.get(Comment, comment_id)

    # Check if the comment exists
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    # Delete the comment
    CommentService.delete_comment(comment_id)

    return jsonify({
        "message": "Comment deleted successfully"
    }), 200
