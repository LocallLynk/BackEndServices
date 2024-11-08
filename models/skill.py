from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import ForeignKey
from models.neighborSkill import neighbor_skill


class Skill(Base):
    __tablename__ = 'skill'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    experience: Mapped[str] = mapped_column(db.String(255), nullable=False)
    description: Mapped[str] = mapped_column(db.String(255), nullable=False)
    
    neighbor: Mapped[List["Neighbor"]] = relationship("Neighbor", secondary=neighbor_skill, back_populates="skills")

    # Relationship for tasks associated with this skill
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="skill")

    