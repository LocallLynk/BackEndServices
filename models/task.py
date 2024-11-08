from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import ForeignKey
# from models import Neighbor, Skill, Task, Feedback
# from models.neighbor import Neighbor
# from models.skill import Skill
# from models.feedback import Feedback
class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(db.String(255), nullable=False)
    created_on: Mapped[date] = mapped_column(db.Date, default=date.today())
    status: Mapped[str] = mapped_column(db.String(255), nullable=False)
    task_paid: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    traded_task: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    task_neighbor_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    client_neighbor_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    skill_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('skill.id'), nullable=False)
    
    # Define relationships and clarify foreign keys

    task_neighbor: Mapped["Neighbor"] = relationship("Neighbor", foreign_keys=[task_neighbor_id], back_populates="tasks_as_task_neighbor")
    client_neighbor: Mapped["Neighbor"] = relationship("Neighbor", foreign_keys=[client_neighbor_id], back_populates="tasks_as_client_neighbor")
    skill: Mapped["Skill"] = relationship("Skill", back_populates="tasks")
    feedback: Mapped[List["Feedback"]] = relationship("Feedback", back_populates="task")
    
    