from database import db, Base
from models import Post, Neighbor, Comment, Like, Dislike, Share
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def create_post(db: Session, post: Post):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.post_id == post_id).first()

def get_all_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def get_posts_by_neighbor_id(db: Session, neighbor_id: int, skip: int = 0, limit: int = 10):
    return db.query(Post).filter(Post.neighbor_id == neighbor_id).offset(skip).limit(limit).all()

def get_posts_by_zipcode(db: Session, zipcode: str, skip: int = 0, limit: int = 10):
    return db.query(Post).filter(Post.zipcode == zipcode).offset(skip).limit(limit).all()

def update_post(db: Session, post_id: int, post: Post):
    db.execute(update(Post).where(Post.post_id == post_id).values(post))
    db.commit()
    return db.execute(select(Post).where(Post.post_id == post_id)).scalar()

def delete_post(db: Session, post_id: int):
    db.execute(delete(Post).where(Post.post_id == post_id))
    db.commit()
    return None