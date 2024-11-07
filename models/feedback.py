from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import ForeignKey
# from models import Neighbor, Task
from models.neighbor import Neighbor


class Feedback(Base):
    __tablename__ = 'feedback'

    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str] = mapped_column(db.String(255), nullable=True)
    rating: Mapped[int] = mapped_column(db.Integer, nullable=False)
    created_on: Mapped[date] = mapped_column(db.Date, default=date.today())
    reviewer_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    reviewed_neighbor_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('neighbor.id'), nullable=False)
    task_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('task.id'), nullable=False)
   
   
    reviewer: Mapped["Neighbor"] = db.relationship(back_populates="feedback")
    reviewed_neighbor: Mapped["Neighbor"] = db.relationship(back_populates="feedback")
    

