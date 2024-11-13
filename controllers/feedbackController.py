from flask import request, jsonify
from models.schema.feedbackSchema import feedback_schema, feedbacks_schema
from services import NeighborService
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required
from services import FeedbackService

@token_required
def create_feedback():
    try:
        feedback_data = feedback_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_feedback,_ = FeedbackService.create_feedback(feedback_data)

    return jsonify({
        "message": "Feedback added successfully",
        "feedback": feedback_schema.dump(new_feedback)
    }), 201

@token_required
def get_feedback_by_id(feedback_id):
    feedback = FeedbackService.find_feedback_by_id(feedback_id)

    return jsonify({
        "message": "Feedback retrieved successfully",
        "feedback": feedback_schema.dump(feedback)
    }), 200

@token_required
def get_feedback_by_task_id(task_id):
    feedback = FeedbackService.find_feedback_by_task_id(task_id)

    return jsonify({
        "message": "Feedback for the task retrieved successfully",
        "feedback": feedback_schema.dump(feedback)
    }), 200

@token_required
def get_feedback_by_task_neighbor_id(task_neighbor_id):
    feedback = FeedbackService.find_feedback_by_task_neighbor_id(task_neighbor_id)

    return jsonify({
        "message": "Feedback for the task neighbor retrieved successfully",
        "feedback": feedbacks_schema.dump(feedback)
    }), 200

@token_required
def get_feedback_by_client_neighbor_id(client_neighbor_id):
    feedback = FeedbackService.find_feedback_by_client_neighbor_id(client_neighbor_id)

    return jsonify({
        "message": "Feedback for the client neighbor retrieved successfully",
        "feedback": feedbacks_schema.dump(feedback)
    }), 200

@token_required
def update_task_neighbor_feedback_rating(reviewed_neighbor):
    task = FeedbackService.update_task_neighbor_feedback_rating(reviewed_neighbor)

    return jsonify({
        "message": "Feedback rating for task neighbor updated successfully",
        "overall_rating": feedbacks_schema.dump(task)
    }), 200

@token_required
def update_client_neighbor_feedback_rating(reviewer_neighbor):
    client = FeedbackService.update_client_neighbor_feedback_rating(reviewer_neighbor)

    return jsonify({
        "message": "Feedback rating for client neighbor updated successfully",
        "overall_rating": feedbacks_schema.dump(client)
    }), 200

@admin_required
def get_all_feedback():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_feedback = FeedbackService.get_all_feedback(page, per_page)

    return jsonify({
        "message": "All feedback retrieved successfully",
        "feedback": feedbacks_schema.dump(all_feedback, many=True)
    }), 200

@admin_required
def delete_feedback(feedback_id):
    FeedbackService.delete_feedback(feedback_id)

    return jsonify({'message': 'Feedback deleted successfully'}), 200