from database import db, Base
from models.post import Post
from models.dislike import Dislike
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_dislike(dislike_data):
    # Convert dislike_data dictionary to a Dislike instance
    dislike = Dislike(**dislike_data)
    
    # Debug: Log dislike data
    print(f"Dislike Data: {dislike_data}")
    
    # Check if the user has already disliked the post
    existing_dislike = db.session.query(Dislike).filter(
        Dislike.neighbor_id == dislike.neighbor_id, 
        Dislike.post_id == dislike.post_id
    ).first()
    
    # Debug: Log result of existing_dislike query
    print(f"Existing Dislike: {existing_dislike}")
    
    if existing_dislike:
        raise ValueError("You have already disliked this post")
    
    # Check if the post exists
    post = db.session.query(Post).filter(Post.id == dislike.post_id).first()
    if not post:
        raise ValueError("Post not found")
    
    # Increment the dislike count
    post.dislikes_count += 1  
    
    # Save the dislike to the database
    db.session.add(dislike)
    db.session.commit()
    db.session.refresh(dislike)
    return dislike




def remove_dislike(dislike_id):
    # Fetch the Dislike to determine the associated Post
    dislike = db.session.query(Dislike).filter(Dislike.id == dislike_id).first()
    if not dislike:
        raise ValueError("Dislike not found")

    # Fetch the associated Post
    post = db.session.query(Post).filter(Post.id == dislike.post_id).first()
    if post:
        # Decrement the dislikes_count
        post.dislikes_count = max(0, post.dislikes_count - 1)  # Ensure dislikes_count doesn't go below 0

    # Remove the Dislike
    db.session.execute(delete(Dislike).where(Dislike.id == dislike_id))
    db.session.commit()

    return None
