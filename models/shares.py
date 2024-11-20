from datetime import date
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database import db, Base

#Base = declarative_base()
class Share(Base):
    __tablename__ = 'shares'

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    neighbor_id: Mapped[int] = mapped_column(ForeignKey('neighbor.id', ondelete='CASCADE'), nullable=False)
    shared_on: Mapped[date] = mapped_column(default=lambda: date.today())  
    content: Mapped[str] = mapped_column(db.String(255), nullable=False)

    # Relationships
    post: Mapped["Post"] = relationship("Post", back_populates="shares", cascade="all, delete-orphan")  
    neighbor: Mapped["Neighbor"] = relationship("Neighbor", back_populates="shares", cascade="all, delete-orphan") 
   

