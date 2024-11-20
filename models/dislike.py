from datetime import date
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database import db, Base

#Base = declarative_base()
class Dislike(Base):
    __tablename__ = 'dislikes'

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    neighbor_id: Mapped[int] = mapped_column(ForeignKey('neighbor.id'), nullable=False)
    disliked_on: Mapped[date] = mapped_column(default=date.today)

    # Relationships
    post: Mapped["Post"] = relationship("Post", back_populates="dislikes")
    neighbor: Mapped["Neighbor"] = relationship("Neighbor", back_populates="dislikes")
