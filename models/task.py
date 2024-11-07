from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from models.skill import Skill
from models.feedback import Feedback
from models.neighbor import Neighbor

class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    description = Mapped[str] = mapped_column(db.String(255), nullable=False)
    created_on = Mapped[date] = mapped_column(db.Date, default=date.today())
    status = Mapped[str] = mapped_column(db.String(255), nullable=False)
    task_paid = Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    traded_task = Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    task_neighbor_id = Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    client_neighbor_id = Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    skill_id = Mapped[int] = mapped_column(db.Integer, ForeignKey('skill.id'), nullable=False)
    
    
    
    
    neighbor = Mapped[Neighbor] = mapped_column(relationship("Neighbor", back_populates="task"))
    skill = Mapped[Skill] = mapped_column(relationship("Skill", back_populates="task"))
    feedback = Mapped[List[Feedback]] = mapped_column(relationship("Feedback", back_populates="task"))
    
    