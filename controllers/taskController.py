from flask import request, jsonify
from models.schemas.skillSchema import skill_schema
from models.schemas.neighborSchema import neighbors_schema, neighbor_schema
from services import SkillService
from models.skill import Skill
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required
from models.task import Task
from models.feedback import Feedback
from services import FeedbackService
from services import NeighborService
from models.neighbor import Neighbor
from services import TaskService
from models.task import Task
from models.schemas.taskSchema import task_schema

@token_required
def create_task():
    try:
        task_data = task_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_task = TaskService.create_task(task_data)

    return task_schema.jsonify(new_task), 201

@admin_required
def get_all_tasks():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_tasks = TaskService.get_all_tasks(page, per_page)

    return task_schema.jsonify(all_tasks), 200

@token_required
def get_task_by_id(task_id):
    task = TaskService.find_task_by_id(task_id)

    return task_schema.jsonify(task), 200

@token_required
def get_task_by_task_neighbor_id(task_neighbor_id):
    task = TaskService.find_task_by_task_neighbor_id(task_neighbor_id)

    return task_schema.jsonify(task), 200

@token_required
def get_task_by_client_neighbor_id(client_neighbor_id):
    task = TaskService.find_task_by_client_neighbor_id(client_neighbor_id)

    return task_schema.jsonify(task), 200

@token_required
def update_task(task_id):
    try:
        task_data = task_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_task = TaskService.update_task(task_id, task_data)

    return task_schema.jsonify(updated_task), 200

@token_required
def delete_task(task_id):
    TaskService.delete_task(task_id)

    return jsonify({'message': 'Task deleted successfully'}), 200

@token_required
def update_task_status(task_id):
    try:
        task_data = task_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_task = TaskService.update_task_status(task_id, task_data)

    return task_schema.jsonify(updated_task), 200

@token_required
def update_task_paid(task_id):
    try:
        task_data = task_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_task = TaskService.update_task_paid(task_id, task_data)

    return task_schema.jsonify(updated_task), 200

@token_required
def update_traded_task(task_id):
    try:
        task_data = task_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_task = TaskService.update_traded_task(task_id, task_data)

    return task_schema.jsonify(updated_task), 200







