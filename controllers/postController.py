from flask import request, jsonify
from models.schema.postSchema import post_schema, posts_schema
from services import PostService
from marshmallow import ValidationError
from utils.util import token_required, admin_required

@token_required
def create_post():
    try:
        post_data = post_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    new_post = PostService.create_post(post_data)
    return jsonify({
        "message": "Post created successfully",
        "post": post_schema.dump(new_post)
    }), 201

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
    post = PostService.find_post_by_id(post_id)
    return jsonify({
        "message": "Post retrieved successfully",
        "post": post_schema.dump(post)
    }), 200

@token_required
def get_posts_by_neighbor_id(neighbor_id):
    posts = PostService.find_posts_by_neighbor_id(neighbor_id)
    return jsonify({
        "message": "Posts by neighbor ID retrieved successfully",
        "posts": posts_schema.dump(posts)
    }), 200

@token_required
def get_posts_by_zipcode(zipcode):
    posts = PostService.find_posts_by_zipcode(zipcode)
    return jsonify({
        "message": "Posts by zipcode retrieved successfully",
        "posts": posts_schema.dump(posts)
    }), 200

@token_required
def update_post(post_id):
    try:
        post_data = post_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    updated_post = PostService.update_post(post_id, post_data)
    return jsonify({
        "message": "Post updated successfully",
        "post": post_schema.dump(updated_post)
    }), 200

@token_required
def delete_post(post_id):
    PostService.delete_post(post_id)
    return jsonify({
        "message": "Post deleted successfully"
    }), 200