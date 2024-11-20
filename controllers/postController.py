from flask import request, jsonify
from models.schema.postSchema import post_schema, posts_schema
from services import PostService
from marshmallow import ValidationError
from utils.util import token_required, admin_required
from sqlalchemy.orm import Session
from services.PostService import create_post as create_post_service
from database import db 
# from flask_login import current_user
from utils.util import get_current_user
from models.post import Post



@token_required
def create_post():
    # Add current user's neighbor_id to post data
    neighbor_id = get_current_user()
    request.json['neighbor_id'] = neighbor_id
   
    try:
        # Validate input using the schema
        post_data = post_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    try:
       # Call the service to create the post
        new_post = create_post_service(post_data)

        # Return the created post
        return jsonify({
            "message": "Post created successfully",
            "post": post_schema.dump(new_post)
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@admin_required
def get_all_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_posts = PostService.get_all_posts()
    return jsonify({
        "message": "All posts retrieved successfully",
        "posts": posts_schema.dump(all_posts, many=True)
    }), 200

@token_required
def get_post_by_id(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return jsonify({
        "message": "Post retrieved successfully",
        "post": post_schema.dump(post)
    }), 200

@token_required
def get_posts_by_neighbor_id(neighbor_id):
    posts = PostService.get_posts_by_neighbor_id(neighbor_id)
    if not posts:
        return jsonify({"error": "No posts found for neighbor"}), 404
    return jsonify({
        "message": "Posts by neighbor ID retrieved successfully",
        "posts": posts_schema.dump(posts)
    }), 200

@token_required
def update_post(post_id):
    # Get the current user from the token
    neighbor_id = get_current_user()

    # Fetch the post from the database
    post = Post.query.get(post_id)

    # Check if the post exists
    if not post:
        return jsonify({"error": "Post not found"}), 404

    # Check if the current user is the owner of the post
    if Post.neighbor_id != neighbor_id:
        return jsonify({"error": "You are not the owner of this post"}), 403

    # Validate the input data
    try:
        post_data = post_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    # Update the post
    updated_post = PostService.update_post(post_id, post_data)

    return jsonify({
        "message": "Post updated successfully",
        "post": post_schema.dump(updated_post)
    }), 200


@token_required
def delete_post(post_id):
    # Get the current user from the token
    neighbor_id = get_current_user()

    # Fetch the post from the database
    post = Post.query.get(post_id)

    # Check if the post exists
    if not post:
        return jsonify({"error": "Post not found"}), 404

    # Check if the current user is the owner of the post
    if Post.neighbor_id != neighbor_id:
        return jsonify({"error": "You are not the owner of this post"}), 403

    # Delete the post
    PostService.delete_post(post_id)

    return jsonify({
        "message": "Post deleted successfully"
    }), 200
