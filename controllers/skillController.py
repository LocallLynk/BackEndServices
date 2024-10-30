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

@token_required
def create_skill():
    try:
        skill_data = skill_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_skill = SkillService.create_skill(skill_data)

    return skill_schema.jsonify(new_skill), 201

@token_required
def get_skill_by_id(skill_id):
    skill = SkillService.find_skill_by_id(skill_id)

    return skill_schema.jsonify(skill), 200

@token_required
def get_skill_by_name(skill_name):
    skill = SkillService.find_skill_by_name(skill_name)

    return skill_schema.jsonify(skill), 200

@admin_required
def update_skill(current_skill):
    try:
        skill_data = skill_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_skill = SkillService.update_skill(current_skill, skill_data)

    return skill_schema.jsonify(updated_skill), 200

@admin_required
def delete_skill(skill_id):
    SkillService.delete_skill(skill_id)

    return jsonify({'message': 'Skill deleted successfully'}), 200

@token_required
def get_all_skills():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_skills = SkillService.get_all_skills(page, per_page)

    return skill_schema.jsonify(all_skills), 200

@token_required
def get_skill_by_neighbor_id(neighbor_id):
    skill = SkillService.find_skill_by_neighbor_id(neighbor_id)

    return skill_schema.jsonify(skill), 200

@token_required
def get_skill_by_zipcode(zipcode):
    skill = SkillService.find_skill_by_zipcode(zipcode)

    return skill_schema.jsonify(skill), 200

@token_required
def get_neighbors_by_skill(skill_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = SkillService.get_neighbor_by_skill(skill_id, page, per_page)

    return neighbors_schema.jsonify(all_neighbors), 200

@token_required
def remove_skill_from_neighbor(neighbor_id, skill_id):
    SkillService.remove_skill_from_neighbor(neighbor_id, skill_id)

    return jsonify({'message': 'Skill removed successfully'}), 200

@token_required
def add_skill_to_neighbor(neighbor_id, skill_id):
    SkillService.add_skill_to_neighbor(neighbor_id, skill_id)

    return jsonify({'message': 'Skill added successfully'}), 200



