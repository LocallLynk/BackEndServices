from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from sqlalchemy import ForeignKey
from models.neighborSkill import neighbor_skill
from models.feedback import Feedback
from models.task import Task
from models.skill import Skill
from models.post import Post
# from models.comment import Comment
# from models.like import Like
# from models.dislike import Dislike
# from models.shares import Share

from typing import TYPE_CHECKING


print("Importing Neighbor model...")
if TYPE_CHECKING:
    from models.post import Post
    print("Post successfully imported in Neighbor.")


class Neighbor(Base):
    __tablename__ = 'neighbor'

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_pic: Mapped[str] = mapped_column(db.String(255), nullable=True)  # Storing the path to the profile picture
    first_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(25), nullable=False)
    zipcode: Mapped[str] = mapped_column(db.String(10), nullable=False)
    username: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(db.LargeBinary, nullable=False)  # Storing hashed password as bytes
    salt: Mapped[bytes] = mapped_column(db.LargeBinary, nullable=False)  # Adding salt as a binary column
    overall_rating: Mapped[float] = mapped_column(db.Float, default=0.0)
    num_ratings: Mapped[int] = mapped_column(db.Integer, default=0)
    num_rated: Mapped[int] = mapped_column(db.Integer, default=0)
    created_on: Mapped[date] = mapped_column(db.Date, default=date.today())
    task_neighbor: Mapped[bool] = mapped_column(db.Boolean, default=None, nullable=True)
    client_neighbor: Mapped[bool] = mapped_column(db.Boolean, default=None, nullable=True)
    admin: Mapped[bool] = mapped_column(db.Boolean, default=False, nullable=True)
    
    skills: Mapped[List["Skill"]] = relationship("Skill", secondary=neighbor_skill, back_populates="neighbor")

    # Relationships to feedback
    given_feedback: Mapped[List["Feedback"]] = relationship("Feedback", foreign_keys="[Feedback.reviewer_id]", back_populates="reviewer", cascade="all, delete-orphan")
    received_feedback: Mapped[List["Feedback"]] = relationship("Feedback", foreign_keys="[Feedback.reviewed_neighbor_id]", back_populates="reviewed_neighbor", cascade="all, delete-orphan")
   
    # Relationships for Task as task neighbor and client neighbor
    tasks_as_task_neighbor: Mapped[List["Task"]] = relationship("Task", foreign_keys="[Task.task_neighbor_id]", back_populates="task_neighbor", cascade="all, delete-orphan")
    tasks_as_client_neighbor: Mapped[List["Task"]] = relationship("Task", foreign_keys="[Task.client_neighbor_id]", back_populates="client_neighbor", cascade="all, delete-orphan")

    # Social interactions - cascade deletion
    posts = relationship("Post", back_populates="neighbor", cascade="all, delete-orphan", lazy="select")
    comments = relationship("Comment", back_populates="neighbor", cascade="all, delete-orphan", lazy="select")
    likes = relationship("Like", back_populates="neighbor", cascade="all, delete-orphan", lazy="select")
    dislikes = relationship("Dislike", back_populates="neighbor", cascade="all, delete-orphan", lazy="select")
    shares = relationship("Share", back_populates="neighbor", cascade="all, delete-orphan", lazy="select")
