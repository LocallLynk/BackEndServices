from flask import Blueprint
from controllers.taskController import taskController

task_blueprint = Blueprint('task_bp', __name__)

#url_prefix='/task'

task_blueprint.route('/task', methods=['POST'])(create_task)
task_blueprint.route('/task', methods=['GET'])(get_all_tasks)
task_blueprint.route('/task/<task_id>', methods=['GET'])(get_task_by_id)
task_blueprint.route('/task/task_neighbor/<task_neighbor_id>', methods=['GET'])(get_task_by_task_neighbor_id)
task_blueprint.route('/task/client_neighbor/<client_neighbor_id>', methods=['GET'])(get_task_by_client_neighbor_id)
task_blueprint.route('/task/<task_id>', methods=['PUT'])(update_task)
task_blueprint.route('/task/<task_id>', methods=['DELETE'])(delete_task)
task_blueprint.route('task/<task_id>/status/<new_status>', methods=['PUT'])(update_task_status)
task_blueprint.route('task/<task_id>/paid/<task_paid>', methods=['PUT'])(update_task_paid)
task_blueprint.route('task/<task_id>/traded/<traded_task>', methods=['PUT'])(update_traded_task)
