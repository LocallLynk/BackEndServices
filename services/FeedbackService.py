from database import db  # services interact directly with the db
from models.neighbor import Neighbor
from models.feedback import Feedback
from datetime import date
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify

def create_feedback(feedback_data):
    new_feedback = Feedback(
        task_neighbor_id=feedback_data['reviewed_neighbor_id'],
        task_id=feedback_data['task_id'],
        rating=feedback_data['rating'],
        client_neighbor_id=feedback_data['reviewer_id'],
        comment=feedback_data['comment'],
        created_on=date.today()
    )
    
    db.session.add(new_feedback)
    db.session.commit()
    db.session.refresh(new_feedback)  # refresh to get the ID of new feedback

    return new_feedback

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
    feedbacks = result.scalars().all()  # Get all feedbacks for the task

    return feedbacks  # Return all matching feedbacks

def find_feedback_by_task_neighbor_id(task_neighbor_id):
    query = select(Feedback).where(Feedback.task_neighbor_id == task_neighbor_id)
    result = db.session.execute(query)
    feedbacks = result.scalars().all()

    return feedbacks

def find_feedback_by_client_neighbor_id(client_neighbor_id):
    query = select(Feedback).where(Feedback.client_neighbor_id == client_neighbor_id)
    result = db.session.execute(query)
    feedbacks = result.scalars().all()

    return feedbacks

def update_task_neighbor_feedback_rating(task_neighbor_id, feedback):
    neighbor = db.session.get(Neighbor, task_neighbor_id)
    if not neighbor:
        raise ValueError("Neighbor with this ID not found.")

    neighbor.num_ratings += 1
    new_rating = feedback['rating']
    overall_rating = (neighbor.rating * (neighbor.num_ratings - 1) + new_rating) / neighbor.num_ratings
    neighbor.rating = overall_rating

    db.session.commit()

    return overall_rating

def update_client_neighbor_feedback_rating(client_neighbor_id, feedback):
    client_neighbor = db.session.get(Neighbor, client_neighbor_id)
    if not client_neighbor:
        raise ValueError("Client neighbor with this ID not found.")

    client_neighbor.num_ratings += 1
    new_rating = feedback['rating']
    overall_rating = (client_neighbor.rating * (client_neighbor.num_ratings - 1) + new_rating) / client_neighbor.num_ratings
    client_neighbor.rating = overall_rating

    db.session.commit()

    return overall_rating

def delete_feedback(feedback_id):
    feedback = db.session.get(Feedback, feedback_id)
    if not feedback:
        raise ValueError("Feedback with this ID not found.")

    db.session.delete(feedback)
    db.session.commit()

    return jsonify({"message": "Feedback deleted successfully"}), 200


