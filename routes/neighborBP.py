from flask import Blueprint
from controllers.neighborController import create_neighbor, get_all_neighbors, get_neighbor_by_id, get_neighbor_by_username, get_neighbor_by_email, get_neighbor_by_zipcode, get_neighbor_by_skill, get_neighbor_by_task, get_neighbor_by_feedback, get_neighbor_by_rating, update_neighbor, delete_neighbor, add_skill_to_neighbor

neighbor_blueprint = Blueprint('neighbor_bp', __name__)

#url_prefix='/neighbor'

neighbor_blueprint.route('/', methods=['POST'])(create_neighbor)
neighbor_blueprint.route('/', methods=['GET'])(get_all_neighbors)
neighbor_blueprint.route('/<neighbor_id>', methods=['GET'])(get_neighbor_by_id)
neighbor_blueprint.route('/username/<username>', methods=['GET'])(get_neighbor_by_username)
neighbor_blueprint.route('/email/<email>', methods=['GET'])(get_neighbor_by_email)
neighbor_blueprint.route('/zipcode/<zipcode>', methods=['GET'])(get_neighbor_by_zipcode)
neighbor_blueprint.route('/skill/<skill_id>', methods=['GET'])(get_neighbor_by_skill)
neighbor_blueprint.route('/task/<task_id>', methods=['GET'])(get_neighbor_by_task)
neighbor_blueprint.route('/feedback/<feedback_id>', methods=['GET'])(get_neighbor_by_feedback)
neighbor_blueprint.route('/rating/<rating>', methods=['GET'])(get_neighbor_by_rating)
neighbor_blueprint.route('/<neighbor_id>', methods=['PUT'])(update_neighbor)
neighbor_blueprint.route('/<neighbor_id>', methods=['DELETE'])(delete_neighbor)
neighbor_blueprint.route('/<neighbor_id>/skills', methods=['POST'])(add_skill_to_neighbor)