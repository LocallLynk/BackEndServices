from flask import request, jsonify
from models.schema.taskSchema import task_schema, tasks_schema
from services import TaskService
from marshmallow import ValidationError
from utils.util import token_required, admin_required

@token_required
def create_task():
    try:
        task_data = task_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    new_task = TaskService.create_task(task_data)
    return jsonify({
        "message": "Task created successfully",
        "task": task_schema.dump(new_task)
    }), 201

@admin_required
def get_all_tasks():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_tasks = TaskService.get_all_tasks()
    return jsonify({
        "message": "All tasks retrieved successfully",
        "tasks": tasks_schema.dump(all_tasks, many=True)
    }), 200

#@token_required
def get_task_by_id(task_id):
    task = TaskService.find_task_by_id(task_id)
    return jsonify({
        "message": "Task retrieved successfully",
        "task": task_schema.dump(task)
    }), 200

#@token_required
def get_task_by_task_neighbor_id(task_neighbor_id):
    task = TaskService.find_tasks_by_task_neighbor_id(task_neighbor_id)
    return jsonify({
        "message": "Tasks by task neighbor ID retrieved successfully",
        "task": tasks_schema.dump(task)
    }), 200

#@token_required
def get_task_by_client_neighbor_id(client_neighbor_id):
    task = TaskService.find_tasks_by_client_neighbor_id(client_neighbor_id)
    return jsonify({
        "message": "Task by client neighbor ID retrieved successfully",
        "task": tasks_schema.dump(task)
    }), 200

#@token_required
def update_task(task_id):
    try:
        task_data = task_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    updated_task = TaskService.update_task(task_id, task_data)
    return jsonify({
        "message": "Task updated successfully",
        "task": task_schema.dump(updated_task)
    }), 200

@token_required
def delete_task(task_id):
    TaskService.delete_task(task_id)
    return jsonify({"message": "Task deleted successfully"}), 200






