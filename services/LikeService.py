from database import db, Base
from models.post import Post
from models.like import Like
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_like(db: Session, like: Like):
    db.add(like)
    existing_like = db.query(Like).filter(Like.neighbor_id == like.neighbor_id, Like.post_id == like.post_id).first()
    if existing_like:
        raise ValueError("User has already liked this post")

    post = db.query(Post).filter(Post.post_id == like.post_id).first()
    if not post:
        raise ValueError("Post not found")
    post.likes_count += 1  
    db.commit()
    db.refresh(like)
    return like

def remove_like(db: Session, like_id: int):
    # Fetch the Like to determine the associated Post
    like = db.query(Like).filter(Like.like_id == like_id).first()
    if not like:
        raise ValueError("Like not found")

    # Fetch the associated Post
    post = db.query(Post).filter(Post.post_id == like.post_id).first()
    if post:
        # Decrement the likes_count
        post.likes_count = max(0, post.likes_count - 1)  # Ensure likes_count doesn't go below 0

    # Remove the Like
    db.execute(delete(Like).where(Like.like_id == like_id))
    db.commit()

    return None
