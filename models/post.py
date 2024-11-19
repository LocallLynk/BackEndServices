from datetime import date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey
from database import db, Base
from typing import List, TYPE_CHECKING
from models.like import Like
from models.dislike import Dislike
from models.shares import Share
from models.comment import Comment

print("Importing post model...")

if TYPE_CHECKING:
    from models.comment import Comment  # Import for type checking only
    from models.like import Like
    from models.dislike import Dislike
    from models.shares import Share
    from models.neighbor import Neighbor


# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    # Column Definitions
    post_id: Mapped[int] = mapped_column(primary_key=True)
    neighbor_id: Mapped[int] = mapped_column(ForeignKey('neighbor.id'), nullable=False)
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    content: Mapped[str] = mapped_column(db.String(255), nullable=False)
    created_on: Mapped[date] = mapped_column(default=date.today)
    likes_count: Mapped[int] = mapped_column(default=0)
    dislikes_count: Mapped[int] = mapped_column(default=0)
    comments_count: Mapped[int] = mapped_column(default=0)
    shares_count: Mapped[int] = mapped_column(default=0)

    # Relationships
    
    neighbor = relationship("Neighbor", back_populates="posts")
    likes = relationship("Like", back_populates="post", cascade="all, delete-orphan", lazy="select")
    dislikes = relationship("Dislike", back_populates="post", cascade="all, delete-orphan", lazy="select")
    shares = relationship("Share", back_populates="post", cascade="all, delete-orphan", lazy="select")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan", lazy="select")

    




