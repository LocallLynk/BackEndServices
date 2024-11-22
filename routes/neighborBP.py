from flask import Blueprint
from controllers.neighborController import create_neighbor, get_all_neighbors, get_neighbor_by_id, get_neighbor_by_username, get_neighbor_by_email, get_neighbor_by_zipcode, update_neighbor, delete_neighbor, make_admin, login, remove_admin         

neighbor_blueprint = Blueprint('neighbor_bp', __name__)

#url_prefix='/neighbor'

neighbor_blueprint.route('/', methods=['POST'])(create_neighbor)
neighbor_blueprint.route('/', methods=['GET'])(get_all_neighbors)
neighbor_blueprint.route('/login', methods=['POST'])(login)
neighbor_blueprint.route('/admin/<neighbor_id>', methods=['PUT'])(make_admin)
neighbor_blueprint.route('/admin/<neighbor_id>', methods=['DELETE'])(remove_admin)
neighbor_blueprint.route('/<neighbor_id>', methods=['GET'])(get_neighbor_by_id)
neighbor_blueprint.route('/username/<username>', methods=['GET'])(get_neighbor_by_username)
neighbor_blueprint.route('/email/<email>', methods=['GET'])(get_neighbor_by_email)
neighbor_blueprint.route('/zipcode/<zipcode>', methods=['GET'])(get_neighbor_by_zipcode)
neighbor_blueprint.route('/<neighbor_id>', methods=['PUT'])(update_neighbor) 
neighbor_blueprint.route('/<neighbor_id>', methods=['DELETE'])(delete_neighbor)
