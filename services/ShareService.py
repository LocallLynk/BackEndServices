from database import db, Base
from models.shares import Share
from models.post import Post
from datetime import datetime
from sqlalchemy import select, update, delete
from typing import List

def add_share(share_data):
    # Ensure `share_data` is a dictionary and not already a `Share` instance
    if isinstance(share_data, dict):
        share = Share(**share_data)  # Convert dictionary to Share instance
    elif isinstance(share_data, Share):
        share = share_data  # Use the provided Share instance as-is
    else:
        raise ValueError("Invalid share data type. Expected dict or Share instance.")

    # Check if the user has already shared the post
    existing_share = (
        db.session.query(Share)
        .filter(Share.neighbor_id == share.neighbor_id, Share.post_id == share.post_id)
        .first()
    )
    if existing_share:
        raise ValueError("You have already shared this post")

    # Check if the post exists
    post = db.session.query(Post).filter(Post.id == share.post_id).first()
    if not post:
        raise ValueError("Post not found")

    # Increment the share count
    post.shares_count += 1

    # Save the share to the database
    db.session.add(share)
    db.session.commit()
    db.session.refresh(share)

    return share


def remove_share(share_id):
    share = db.session.query(Share).filter(Share.id == share_id).first()
    if not share:
        raise ValueError("Share not found")
    post = db.session.query(Post).filter(Post.id == share.post_id).first()
    if post:
        post.shares_count = max(0, post.shares_count - 1)
    db.session.execute(delete(Share).where(Share.id == share_id))
    db.session.commit()
    return None

def get_share_by_id(share_id):
    try:
        share = db.session.query(Share).filter(Share.id == share_id).first()
        return share
    except Exception as e:
        raise RuntimeError(f"Error fetching share by ID: {share_id}") from e


def update_share(share_id, share):
    db.session.execute(
        update(Share).where(Share.id == share_id).values(share)
    )
    db.session.commit()
    return db.session.execute(select(Share).where(Share.id == share_id)).scalar()
