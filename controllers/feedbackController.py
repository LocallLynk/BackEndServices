from flask import request, jsonify
from models.schemas.feedbackSchema import feedback_schema
from services import NeighborService
from models.neighbor import Neighbor
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required
from models.task import Task
from models.feedback import Feedback

def create_feedback():
    try:
        feedback_data = feedback_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_feedback = FeedbackService.create_feedback(feedback_data)

    return feedback_schema.jsonify(new_feedback), 201