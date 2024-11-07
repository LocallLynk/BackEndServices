from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import ForeignKey
# from models import Neighbor, Skill, Task, Feedback

class Skill(Base):
    __tablename__ = 'skill'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    experience: Mapped[int] = mapped_column(db.String(255), nullable=False)
    description: Mapped[str] = mapped_column(db.String(255), nullable=False)

    neighbor_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'))

    