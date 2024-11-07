from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from models.skill import Skill
from models.feedback import Feedback
from models.task import Task

class Neighbor(Base):
    __tablename__ = 'neighbor'

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Mapped[str] = mapped_column(db.String(255), nullable=False)
    email = Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone = Mapped[str] = mapped_column(db.String(25), nullable=False)
    zipcode = Mapped[str] = mapped_column(db.String(10), nullable=False)
    username = Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    password = Mapped[str] = mapped_column(db.String(255), nullable=False)
    overall_rating = Mapped[float] = mapped_column(db.Float, default=0.0)
    num_ratings = Mapped[int] = mapped_column(db.Integer, default=0)
    num_rated = Mapped[int] = mapped_column(db.Integer, default=0)
    created_on = Mapped[date] = mapped_column(db.Date, default=date.today())
    task_neighbor = Mapped[bool] = mapped_column(db.Boolean, default=None, nullable=True)
    client_neighbor = Mapped[bool] = mapped_column(db.Boolean, default=None, nullable=True)
    admin = Mapped[bool] = mapped_column(db.Boolean, default=False)
    # salt = Mapped[str] = mapped_column(db.String(255), nullable=False)


    skills = Mapped[List[Skill]] = mapped_column(relationship("Skill", secondary="neighbor_skill", back_populates="neighbors"))
    task = Mapped[List[Task]] = mapped_column(relationship("Task", back_populates="neighbor"))
    feedback = Mapped[List[Feedback]] = mapped_column(relationship("Feedback", back_populates="neighbor"))

