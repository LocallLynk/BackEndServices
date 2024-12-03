from flask import Blueprint
from controllers.neighborController import create_neighbor, get_all_neighbors, get_neighbor_by_id, get_neighbor_by_username, get_neighbor_by_email, get_neighbor_by_zipcode, update_neighbor, delete_neighbor, make_admin, login, remove_admin, validate_user, home_feed        

neighbor_blueprint = Blueprint('neighbor_bp', __name__)

#url_prefix='/neighbor'

neighbor_blueprint.route('/feed', methods=['GET'])(home_feed)
neighbor_blueprint.route('/register', methods=['POST'])(create_neighbor)
neighbor_blueprint.route('/validate', methods=['POST'])(validate_user)
neighbor_blueprint.route('/get', methods=['GET'])(get_all_neighbors)
neighbor_blueprint.route('/login', methods=['POST'])(login)
neighbor_blueprint.route('/make_admin/<neighbor_id>', methods=['PUT'])(make_admin)
neighbor_blueprint.route('/remove_admin/<neighbor_id>', methods=['DELETE'])(remove_admin)
neighbor_blueprint.route('/get/<neighbor_id>', methods=['GET'])(get_neighbor_by_id)
neighbor_blueprint.route('/get/username/<username>', methods=['GET'])(get_neighbor_by_username)
neighbor_blueprint.route('/get/email/<email>', methods=['GET'])(get_neighbor_by_email)
neighbor_blueprint.route('/get/zipcode/<zipcode>', methods=['GET'])(get_neighbor_by_zipcode)
neighbor_blueprint.route('/update/<neighbor_id>', methods=['PUT'])(update_neighbor) 
neighbor_blueprint.route('/delete/<neighbor_id>', methods=['DELETE'])(delete_neighbor)
