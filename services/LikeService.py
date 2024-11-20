from database import db, Base
from models.post import Post
from models.like import Like
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_like(like):
    if isinstance(like, dict):
        like = Like(**like)
    elif isinstance(like, Like):
        like = like
    else:
        raise ValueError("Invalid like data type. Expected dict or Like instance.")
    db.session.add(like)
    existing_like = db.session.query(Like).filter(
        Like.neighbor_id == like.neighbor_id, Like.post_id == like.post_id
    ).first()
    if existing_like:
        raise ValueError("You have already liked this post")

    post = db.session.query(Post).filter(Post.id == like.post_id).first()
    if not post:
        raise ValueError("Post not found")
    post.likes_count += 1
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
