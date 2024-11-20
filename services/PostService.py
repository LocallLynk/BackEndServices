from database import db, Base
from models.post import Post
from sqlalchemy.orm import Session
from typing import List, Optional


def create_post(post_data):

    # Create the new post object
    new_post = Post(**post_data)

    # Save to database
    db.session.add(new_post)
    db.session.commit()
    db.session.refresh(new_post)

    return new_post

def get_post_by_id(post_id):
    post = db.session.query(Post).filter(Post.id == post_id).one_or_none()
    if post is None:
        raise ValueError(f"Post with ID {post_id} not found")
    return post

def get_all_posts(skip: int = 0, limit: int = 10) -> List[Post]:
    return db.session.query(Post).offset(skip).limit(limit).all()

def get_posts_by_neighbor_id(neighbor_id, skip: int = 0, limit: int = 10) -> List[Post]:
    posts = (
        db.session.query(Post)
        .filter(Post.neighbor_id == neighbor_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    if not posts:
        raise ValueError(f"No posts found for neighbor with ID {neighbor_id}")
    return posts

def update_post(post_id, updated_data):
    db.session.query(Post).filter(Post.id == post_id).update(updated_data, synchronize_session="fetch")
    db.session.commit()
    return get_post_by_id(post_id)

def delete_post(post_id) -> None:
    db.session.query(Post).filter(Post.id == post_id).delete()
    db.session.commit()
