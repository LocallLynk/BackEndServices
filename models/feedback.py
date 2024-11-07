from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from models.skill import Skill
from models.neighbor import Neighbor
from models.task import Task

class Feedback(Base):
    __tablename__ = 'feedback'

    id: Mapped[int] = mapped_column(primary_key=True)
    comment = Mapped[str] = mapped_column(db.String(255), nullable=True)
    rating = Mapped[int] = mapped_column(db.Integer, nullable=False)
    created_on = Mapped[date] = mapped_column(db.Date, default=date.today())
    reviewer_id = Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    reviewed_neighbor_id = Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    task_id = Mapped[int] = mapped_column(db.Integer, ForeignKey('task.id'), nullable=False)
    
    
    reviewer = Mapped[Neighbor] = mapped_column(relationship("Neighbor", foreign_keys=[reviewer_id]))
    reviewed_neighbor = Mapped[Neighbor] = mapped_column(relationship("Neighbor", foreign_keys=[reviewed_neighbor_id]))
    task = Mapped[Task] = mapped_column(relationship("Task", back_populates="feedback"))
    
