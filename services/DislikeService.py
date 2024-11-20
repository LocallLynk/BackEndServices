from database import db, Base
from models.post import Post
from models.dislike import Dislike
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_dislike(db: Session, dislike: Dislike):
    db.add(dislike)
    existing_dislike = db.query(Dislike).filter(Dislike.neighbor_id == dislike.neighbor_id, Dislike.post_id == dislike.post_id).first()
    if existing_dislike:
        raise ValueError("You have already disliked this post")
    post = db.query(Post).filter(Post.id == dislike.post_id).first()
    if not post:
        raise ValueError("Post not found")
    post.dislikes_count += 1  
    db.commit()
    db.refresh(dislike)
    return dislike

def remove_dislike(db: Session, dislike_id: int):
    # Fetch the Dislike to determine the associated Post
    dislike = db.query(Dislike).filter(Dislike.id == dislike_id).first()
    if not dislike:
        raise ValueError("Dislike not found")

    # Fetch the associated Post
    post = db.query(Post).filter(Post.id == dislike.post_id).first()
    if post:
        # Decrement the dislikes_count
        post.dislikes_count = max(0, post.dislikes_count - 1)  # Ensure dislikes_count doesn't go below 0

    # Remove the Dislike
    db.execute(delete(Dislike).where(Dislike.id == dislike_id))
    db.commit()

    return None
