from database import db, Base

neighbor_skill = db.Table(
    'neighbor_skill',
    Base.metadata,
    db.Column('neighbor_id', db.ForeignKey('neighbor.id'), primary_key=True),
    db.Column('skill_id', db.ForeignKey('skill.id'), primary_key=True)
)