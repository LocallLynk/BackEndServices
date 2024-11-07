from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from models.skill import Skill
from models.feedback import Feedback
from models.task import Task
from models.neighbor import Neighbor

class Skill(Base):
    __tablename__ = 'skill'

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Mapped[str] = mapped_column(db.String(255), nullable=False)
    experience = Mapped[int] = mapped_column(db.String(255), nullable=False)
    description = Mapped[str] = mapped_column(db.String(255), nullable=False)

    neighbor_id = Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'))

    neighbor = Mapped[List[Neighbor]] = mapped_column(relationship("Neighbor", secondary="neighbor_skill", back_populates="skills"))
    task = Mapped[List[Task]] = mapped_column(relationship("Task", back_populates="skill"))