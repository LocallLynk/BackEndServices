from database import db, Base
from models import Comment, Post
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_comment(db: Session, comment: Comment):
    db.add(comment)

    post = db.query(Post).filter(Post.post_id == comment.post_id).first()
    if not post:
        raise ValueError("Post not found")
    
    post.comments_count += 1
    
    db.commit()
    db.refresh(comment)
    return comment

def get_comment_by_id(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.comment_id == comment_id).first()

def get_comments_by_post_id(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def get_comments_by_neighbor_id(db: Session, neighbor_id: int):
    return db.query(Comment).filter(Comment.neighbor_id == neighbor_id).all()

def get_all_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Comment).offset(skip).limit(limit).all()

def update_comment(db: Session, comment_id: int, comment: Comment):
    db.execute(update(Comment).where(Comment.comment_id == comment_id).values(comment))
    db.commit()

    return db.execute(select(Comment).where(Comment.comment_id == comment_id)).scalar()

def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if not comment:
        raise ValueError("Comment not found")
    
    post = db.query(Post).filter(Post.post_id == comment.post_id).first()
    if post:
        post.comments_count = max(0, post.comments_count - 1)

    db.execute(delete(Comment).where(Comment.comment_id == comment_id))
    db.commit()

    return None