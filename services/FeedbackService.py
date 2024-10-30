from database import db #services interact directly with the db
from models.neighbor import Neighbor
from sqlalchemy import select #so we can query our db
from models.feedback import Feedback
from datetime import date
from models.skill import Skill

def create_feedback(feedback_data):
    new_feedback = Feedback(task_neighbor_id=feedback_data['reviewed_neighbor_id'], 
               task_id=feedback_data['task_id'], rating=feedback_data['rating'],
               client_neighbor_id=feedback_data['reviewer_id'], 
               comment=feedback_data['comment'], created_on=date.today())
    
    db.session.add(new_feedback)
    db.session.commit() #adding the new feedback to the db

    db.session.refresh(new_feedback) #refreshing the db to get the new feedback's id

    return new_feedback

def find_feedback_by_id(feedback_id):
    query = select(Feedback).where(Feedback.id == feedback_id)
    result = db.session.execute(query)
    feedback = result.scalars().first()

    return feedback

def find_feedback_by_task_id(task_id):
    query = select(Feedback).where(Feedback.task_id == task_id)
    result = db.session.execute(query)
    feedback = result.scalars().first()

    return feedback

def find_feedback_by_task_neighbor_id(task_neighbor_id):
    query = select(Feedback).where(Feedback.task_neighbor_id == task_neighbor_id)
    result = db.session.execute(query)
    feedback = result.scalars().first()

    return feedback

def find_feedback_by_client_neighbor_id(client_neighbor_id):
    query = select(Feedback).where(Feedback.client_neighbor_id == client_neighbor_id)
    result = db.session.execute(query)
    feedback = result.scalars().first()

    return feedback

def update_task_neighbor_feedback_rating(task_neighbor_id, feedback):
    query = select(Feedback).where(Feedback.task_neighbor_id == task_neighbor_id)
    result = db.session.execute(query)
    feedback = result.scalars().all()
    
    #add to the number of ratings received

    task_neighbor_id.num_ratings += 1
    
    new_rating = feedback.rating 
    overall_rating = (task_neighbor_id.rating * (task_neighbor_id.num_ratings - 1) 
                      + new_rating) / task_neighbor_id.num_ratings
    db.session.commit()

    return overall_rating

def update_client_neighbor_feedback_rating(client_neighbor_id, feedback):
    query = select(Feedback).where(Feedback.client_neighbor_id == client_neighbor_id)
    result = db.session.execute(query)
    feedback = result.scalars().all()
    
    #add to the number of ratings received

    client_neighbor_id.num_ratings += 1
    
    new_rating = feedback.rating 
    overall_rating = (client_neighbor_id.rating * (client_neighbor_id.num_ratings - 1) 
                      + new_rating) / client_neighbor_id.num_ratings
    db.session.commit()

    return overall_rating

def delete_feedback(feedback_id):
    query = select(Feedback).where(Feedback.id == feedback_id)
    result = db.session.execute(query)
    feedback = result.scalars().first()

    db.session.delete(feedback)
    db.session.commit()

    return feedback

