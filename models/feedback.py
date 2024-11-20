from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import ForeignKey
# from models import Neighbor, Task



class Feedback(Base):
    __tablename__ = 'feedback'

    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str] = mapped_column(db.String(255), nullable=True)
    rating: Mapped[int] = mapped_column(db.Integer, nullable=False)
    created_on: Mapped[date] = mapped_column(db.Date, default=date.today())
    reviewer_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id', ondelete='CASCADE'), nullable=False)
    reviewed_neighbor_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id', ondelete='CASCADE'), nullable=False)
    task_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('task.id', ondelete='CASCADE'), nullable=False)

    reviewer: Mapped["Neighbor"] = relationship("Neighbor", foreign_keys=[reviewer_id], back_populates="given_feedback", cascade="all, delete-orphan")
    reviewed_neighbor: Mapped["Neighbor"] = relationship("Neighbor", foreign_keys=[reviewed_neighbor_id], back_populates="received_feedback", cascade="all, delete-orphan")

    # Relationship back to Task with cascade delete
    task: Mapped["Task"] = relationship("Task", back_populates="feedback", cascade="all, delete-orphan")
    

