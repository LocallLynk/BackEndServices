from flask import Blueprint
from controllers.feedbackController import create_feedback, get_feedback_by_id, get_feedback_by_task_id, get_feedback_by_task_neighbor_id, get_feedback_by_client_neighbor_id, update_task_neighbor_feedback_rating, update_client_neighbor_feedback_rating, delete_feedback, get_all_feedback

feedback_blueprint = Blueprint('feedback_bp', __name__)

#url_prefix='/feedback'

feedback_blueprint.route('/', methods=['POST'])(create_feedback)# trying to implement the update functions. Also, the feedback output is a blank dictionary even though it creates it.
feedback_blueprint.route('/<feedback_id>', methods=['GET'])(get_feedback_by_id)
feedback_blueprint.route('/task/<task_id>', methods=['GET'])(get_feedback_by_task_id)
feedback_blueprint.route('/task_neighbor/<task_neighbor_id>', methods=['GET'])(get_feedback_by_task_neighbor_id)
feedback_blueprint.route('/client_neighbor/<client_neighbor_id>', methods=['GET'])(get_feedback_by_client_neighbor_id)
feedback_blueprint.route('/task_neighbor/<task_neighbor_id>', methods=['PUT'])(update_task_neighbor_feedback_rating) # not working as expected
feedback_blueprint.route('/client_neighbor/<client_neighbor_id>', methods=['PUT'])(update_client_neighbor_feedback_rating) # not working as expected
feedback_blueprint.route('/<feedback_id>', methods=['DELETE'])(delete_feedback)
feedback_blueprint.route('/', methods=['GET'])(get_all_feedback)

