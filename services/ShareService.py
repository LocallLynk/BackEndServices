from database import db, Base
from models.shares import Share
from models.post import Post
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from typing import List

def add_share(db: Session, share: Share):
    db.add(share)
    existing_share = db.query(Share).filter(Share.neighbor_id == share.neighbor_id, Share.post_id == share.post_id).first()
    if existing_share:
        raise ValueError("User has already shared this post")
    post = db.query(Post).filter(Post.post_id == share.post_id).first()
    if not post:
        raise ValueError("Post not found")
    post.shares_count += 1
    db.commit()
    db.refresh(share)
    return share

def remove_share(db: Session, share_id: int):
    share = db.query(Share).filter(Share.share_id == share_id).first()
    if not share:
        raise ValueError("Share not found")
    post = db.query(Post).filter(Post.post_id == share.post_id).first()
    if post:
        post.shares_count = max(0, post.shares_count - 1)
    db.execute(delete(Share).where(Share.share_id == share_id))
    db.commit()
    return None

def get_share_by_id(db: Session, share_id: int):
    return db.query(Share).filter(Share.share_id == share_id).first()

def get_all_shares(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Share).offset(skip).limit(limit).all()

def update_share(db: Session, share_id: int, share: Share):
    db.execute(update(Share).where(Share.share_id == share_id).values(share))
    db.commit()
    return db.execute(select(Share).where(Share.share_id == share_id)).scalar()