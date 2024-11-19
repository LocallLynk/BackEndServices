from datetime import date
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database import db, Base


#Base = declarative_base()
class Comment(Base):
    __tablename__ = 'comments'

    comment_id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.post_id'), nullable=False)
    neighbor_id: Mapped[int] = mapped_column(ForeignKey('neighbor.id'), nullable=False)
    content: Mapped[str] = mapped_column(db.String(255), nullable=False)
    created_on: Mapped[date] = mapped_column(default=date.today)

    # Relationships
    post: Mapped["Post"] = relationship("Post", back_populates="comments")
    neighbor: Mapped["Neighbor"] = relationship("Neighbor", back_populates="comments")
