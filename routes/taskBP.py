from flask import Blueprint
from controllers.taskController import create_task, get_all_tasks, get_task_by_id, get_task_by_task_neighbor_id, get_task_by_client_neighbor_id, update_task, delete_task

task_blueprint = Blueprint('task_bp', __name__)

#url_prefix='/task'

task_blueprint.route('/', methods=['POST'])(create_task)
task_blueprint.route('/', methods=['GET'])(get_all_tasks)
task_blueprint.route('/<task_id>', methods=['GET'])(get_task_by_id)
task_blueprint.route('/task_neighbor/<task_neighbor_id>', methods=['GET'])(get_task_by_task_neighbor_id) # results show in terminal but not in postman
task_blueprint.route('/client_neighbor/<client_neighbor_id>', methods=['GET'])(get_task_by_client_neighbor_id) # results show in terminal but not in postman
task_blueprint.route('/<task_id>', methods=['PUT'])(update_task)
task_blueprint.route('/<task_id>/', methods=['DELETE'])(delete_task)

