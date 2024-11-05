from flask import request, jsonify
from models.schemas.feedbackSchema import feedback_schema
from services import NeighborService
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required
from models.task import Task
from models.feedback import Feedback
from services import FeedbackService

@token_required
def create_feedback():
    try:
        feedback_data = feedback_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_feedback = FeedbackService.create_feedback(feedback_data)

    return feedback_schema.jsonify(new_feedback), 201

@token_required
def get_feedback_by_id(feedback_id):
    feedback = FeedbackService.find_feedback_by_id(feedback_id)

    return feedback_schema.jsonify(feedback), 200

@token_required
def get_feedback_by_task_id(task_id):
    feedback = FeedbackService.find_feedback_by_task_id(task_id)

    return feedback_schema.jsonify(feedback), 200

@token_required
def get_feedback_by_task_neighbor_id(task_neighbor_id):
    feedback = FeedbackService.find_feedback_by_task_neighbor_id(task_neighbor_id)

    return feedback_schema.jsonify(feedback), 200

@token_required
def get_feedback_by_client_neighbor_id(client_neighbor_id):
    feedback = FeedbackService.find_feedback_by_client_neighbor_id(client_neighbor_id)

    return feedback_schema.jsonify(feedback), 200

@token_required
def update_task_neighbor_feedback_rating(task_neighbor_id, feedback):
    FeedbackService.update_task_neighbor_feedback_rating(task_neighbor_id, feedback)

    return jsonify({'message': 'Feedback updated successfully'}), 200

@admin_required
def get_all_feedback():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_feedback = FeedbackService.get_all_feedback(page, per_page)

    return feedback_schema.jsonify(all_feedback), 200

@token_required
def update_client_neighbor_feedback_rating(client_neighbor_id, feedback):
    FeedbackService.update_client_neighbor_feedback_rating(client_neighbor_id, feedback)

    return jsonify({'message': 'Feedback updated successfully'}), 200

@token_required
def update_feedback(feedback_id):
    try:
        feedback_data = feedback_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_feedback = FeedbackService.update_feedback(feedback_id, feedback_data)

    return feedback_schema.jsonify(updated_feedback), 200

@admin_required
def delete_feedback(feedback_id):
    FeedbackService.delete_feedback(feedback_id)

    return jsonify({'message': 'Feedback deleted successfully'}), 200