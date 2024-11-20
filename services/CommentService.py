from database import db, Base
from models.comment import Comment
from models.post import Post
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_comment(comment):
    db.session.add(comment)

    post = db.session.query(Post).filter(Post.id == Comment.post_id).first()
    if not post:
        raise ValueError("Post not found")
    
    post.comments_count += 1
    
    db.session.commit()
    db.session.refresh(comment)
    return comment

def get_comment_by_id(comment_id):
    return db.session.query(Comment).filter(Comment.id == comment_id).first()

def get_comments_by_post_id(post_id):
    return db.session.query(Comment).filter(Comment.post_id == post_id).all()

def get_comments_by_neighbor_id(neighbor_id):
    return db.session.query(Comment).filter(Comment.neighbor_id == neighbor_id).all()

def get_all_comments(skip: int = 0, limit: int = 10):
    return db.session.query(Comment).offset(skip).limit(limit).all()

def update_comment(comment_id, comment):
    db.session.query(Comment).filter(Comment.id == comment_id).update(comment, synchronize_session="fetch")
    db.session.commit()

    return db.session.query(Comment).filter(Comment.id == comment_id).first()

def delete_comment(comment_id):
    comment = db.session.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise ValueError("Comment not found")
    
    post = db.session.query(Post).filter(Post.id == comment.post_id).first()
    if post:
        post.comments_count = max(0, post.comments_count - 1)

    db.session.query(Comment).filter(Comment.id == comment_id).delete()
    db.session.commit()

    return None
