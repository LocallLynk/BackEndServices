from flask import Blueprint
from controllers.skillController import create_skill, get_all_skills, get_skill_by_id, get_skill_by_name, update_skill, delete_skill, get_neighbors_by_skill, remove_skill_from_neighbor, add_skill_to_neighbor

skill_blueprint = Blueprint('skill_bp', __name__)

#url_prefix='/skill'

skill_blueprint.route('/create', methods=['POST'])(create_skill)
skill_blueprint.route('/get', methods=['GET'])(get_all_skills) 
skill_blueprint.route('/get/skill/<skill_id>', methods=['GET'])(get_skill_by_id)
skill_blueprint.route('/get/name/<name>', methods=['GET'])(get_skill_by_name)
skill_blueprint.route('/update/<skill_id>', methods=['PUT'])(update_skill)
skill_blueprint.route('/delete/<skill_id>', methods=['DELETE'])(delete_skill)
skill_blueprint.route('/get/<skill_id>/neighbors', methods=['GET'])(get_neighbors_by_skill)
skill_blueprint.route('/remove/<skill_id>/neighbors/<neighbor_id>', methods=['DELETE'])(remove_skill_from_neighbor)
skill_blueprint.route('/add/<skill_id>/neighbors/<neighbor_id>', methods=['POST'])(add_skill_to_neighbor)




