from flask import Blueprint
from controllers.feedbackController import create_feedback, get_feedback_by_id, get_feedback_by_task_id, get_feedback_by_task_neighbor_id, get_feedback_by_client_neighbor_id, update_task_neighbor_feedback_rating, update_client_neighbor_feedback_rating, delete_feedback, get_all_feedbacks

feedback_blueprint = Blueprint('feedback_bp', __name__)

#url_prefix='/feedback'

feedback_blueprint.route('/feedback', methods=['POST'])(create_feedback)
feedback_blueprint.route('/feedback/<feedback_id>', methods=['GET'])(get_feedback_by_id)
feedback_blueprint.route('/feedback/task/<task_id>', methods=['GET'])(get_feedback_by_task_id)
feedback_blueprint.route('/feedback/task_neighbor/<task_neighbor_id>', methods=['GET'])(get_feedback_by_task_neighbor_id)
feedback_blueprint.route('/feedback/client_neighbor/<client_neighbor_id>', methods=['GET'])(get_feedback_by_client_neighbor_id)
feedback_blueprint.route('/feedback/task_neighbor/<task_neighbor_id>', methods=['PUT'])(update_task_neighbor_feedback_rating)
feedback_blueprint.route('/feedback/client_neighbor/<client_neighbor_id>', methods=['PUT'])(update_client_neighbor_feedback_rating)
feedback_blueprint.route('/feedback/<feedback_id>', methods=['DELETE'])(delete_feedback)
feedback_blueprint.route('/feedback', methods=['GET'])(get_all_feedbacks)

