from database import db, Base
from models.post import Post
from models.like import Like
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_like(like_data):
    # Convert like_data to a Like instance if it's not already
    if not isinstance(like_data, Like):
        like = Like(**like_data)
    else:
        like = like_data

    # Debugging: Log the like data
    print(f"Debug: like_data = {like_data}")

    # Check if the like already exists
    existing_like = db.session.query(Like).filter(
        Like.neighbor_id == like.neighbor_id, Like.post_id == like.post_id
    ).first()
    
    # Debugging: Log existing_like query result
    print(f"Debug: existing_like = {existing_like}")

    if existing_like:
        raise ValueError("You have already liked this post")

    # Check if the post exists
    post = db.session.query(Post).filter(Post.id == like.post_id).first()
    if not post:
        raise ValueError("Post not found")
    
    # Increment the likes count
    post.likes_count += 1

    # Save the like to the database
    db.session.add(like)
    db.session.commit()
    db.session.refresh(like)

    return like


def remove_like(like_id):
    # Fetch the Like to determine the associated Post
    like = db.session.query(Like).filter(Like.id == like_id).first()
    if not like:
        raise ValueError("Like not found")

    # Fetch the associated Post
    post = db.session.query(Post).filter(Post.id == like.post_id).first()
    if post:
        # Decrement the likes_count
        post.likes_count = max(0, post.likes_count - 1)  # Ensure likes_count doesn't go below 0

    # Remove the Like
    db.session.execute(delete(Like).where(Like.id == like_id))
    db.session.commit()

    return None
