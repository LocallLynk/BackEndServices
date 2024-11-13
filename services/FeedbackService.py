from database import db, Base  # services interact directly with the db
from models import Neighbor, Feedback, Task
from datetime import date
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify

from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify

def create_feedback(feedback_data):
    
    rating = feedback_data.get('rating')
    if not isinstance(rating, int) or not (1 <= rating <= 5):
        raise ValueError("Rating must be an integer between 1 and 5")
    
    try:
        
        new_feedback = Feedback(
            reviewed_neighbor_id=feedback_data['reviewed_neighbor_id'],
            task_id=feedback_data['task_id'],
            rating=rating,
            reviewer_id=feedback_data['reviewer_id'],
            comment=feedback_data['comment'],
            created_on=date.today()
        )
        
        db.session.add(new_feedback)
        db.session.commit()
        db.session.refresh(new_feedback)  
        
        reviewed_neighbor = db.session.query(Feedback).filter_by(reviewed_neighbor_id=feedback_data['reviewed_neighbor_id']).all()
       
        if reviewed_neighbor:
            overall_rating = update_task_neighbor_feedback_rating(reviewed_neighbor)
        else:
            raise ValueError("No matching neighbor found to update rating.")
        
        return new_feedback, overall_rating

    except SQLAlchemyError as e:
        db.session.rollback()  # Roll back in case of an error
        print("An error occurred while adding feedback:", e)
        raise ValueError("An error occurred while adding feedback.")
    
        



def find_feedback_by_id(feedback_id):
    query = select(Feedback).where(Feedback.id == feedback_id)
    result = db.session.execute(query)
    feedback = result.scalars().first()

    if not feedback:
        raise ValueError("Feedback with this ID not found.")

    return feedback

def find_feedback_by_task_id(task_id):
    query = select(Feedback).where(Feedback.task_id == task_id)
    result = db.session.execute(query)
    feedbacks = result.scalars().first()  # Get all feedbacks for the task

    return feedbacks  # Return all matching feedbacks

def find_feedback_by_task_neighbor_id(task_neighbor_id):
    reviewed_neighbor_id = task_neighbor_id
    query = select(Feedback).where(Feedback.reviewed_neighbor_id == task_neighbor_id)
    result = db.session.execute(query)
    feedbacks = result.scalars().all()

    return feedbacks

def find_feedback_by_client_neighbor_id(client_neighbor_id):
    reviewer_id = client_neighbor_id
    query = select(Feedback).where(Feedback.reviewer_id == client_neighbor_id)
    result = db.session.execute(query)
    feedbacks = result.scalars().all()

    return feedbacks

def update_task_neighbor_feedback_rating(feedbacks): 
    # calculate the average based on the list of feedbacks
    rating = sum([feedback.rating for feedback in feedbacks]) / len(feedbacks)
    overall_rating = round(rating, 2)
    # get the Neighbor based on its id
    neighbor_id = feedbacks[0].reviewed_neighbor_id
    neighbor = db.session.query(Neighbor).filter_by(id=neighbor_id).first()
    neighbor.num_ratings += 1
    # update the neighbor overall rating attribute
    neighbor.overall_rating = overall_rating
   # commit the changes
    db.session.commit()

    return overall_rating

def delete_feedback(feedback_id):
    feedback = db.session.get(Feedback, feedback_id)
    if not feedback:
        raise ValueError("Feedback with this ID not found.")

    db.session.delete(feedback)
    db.session.commit()

    return None

def get_all_feedback(page=1, per_page=10):
    query = select(Feedback).order_by(Feedback.created_on).limit(per_page).offset((page - 1) * per_page)
    result = db.session.execute(query)
    feedbacks = result.scalars().all()

    return feedbacks


