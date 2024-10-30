from flask import Blueprint
from controllers.skillController import skillController

skill_blueprint = Blueprint('skill_bp', __name__)

#url_prefix='/skill'

skill_blueprint.route('/skill', methods=['POST'])(create_skill)
skill_blueprint.route('/skill', methods=['GET'])(get_all_skills)
skill_blueprint.route('/skill/<skill_id>', methods=['GET'])(get_skill_by_id)
skill_blueprint.route('/skill/name/<name>', methods=['GET'])(get_skill_by_name)
skill_blueprint.route('/skill/<skill_id>', methods=['PUT'])(update_skill)
skill_blueprint.route('/skill/<skill_id>', methods=['DELETE'])(delete_skill)
skill_blueprint.route('/skill/<skill_id>/neighbors', methods=['GET'])(get_neighbors_by_skill)
skill_blueprint.route('/skill/<skill_id>/neighbors', methods=['GET'])(get_skills_by_neighbor)
skill_blueprint.route('/skill/<skill_id>/neighbors/<neighbor_id>', methods=['DELETE'])(remove_neighbor_from_skill)

