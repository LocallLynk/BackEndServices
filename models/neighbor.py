from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import ForeignKey
from models.skill import Skill


class Neighbor(Base):

    __tablename__ = 'neighbor'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(25), nullable=False)
    zipcode: Mapped[str] = mapped_column(db.String(10), nullable=False)
    username: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    overall_rating: Mapped[float] = mapped_column(db.Float, default=0.0)
    num_ratings: Mapped[int] = mapped_column(db.Integer, default=0)
    num_rated: Mapped[int] = mapped_column(db.Integer, default=0)
    created_on: Mapped[date] = mapped_column(db.Date, default=date.today())
    task_neighbor: Mapped[bool] = mapped_column(db.Boolean, default=None, nullable=True)
    client_neighbor: Mapped[bool] = mapped_column(db.Boolean, default=None, nullable=True)
    admin: Mapped[bool] = mapped_column(db.Boolean, default=False)
    skill_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('skill.id'))


    skills: Mapped[List["Skill"]] = db.relationship(back_populates="neighbor")
   

