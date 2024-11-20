from flask import request, jsonify
from models.schema.skillSchema import skill_schema, skills_schema
from models.schema.neighborSchema import neighbors_schema, neighbor_schema
from services import SkillService
from marshmallow import ValidationError
from utils.util import token_required, admin_required, get_current_user


@admin_required
def create_skill():
    try:
        skill_data = skill_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    new_skill = SkillService.create_skill(skill_data)
    return jsonify({
        "message": "Skill created successfully",
        "skill": skill_schema.dump(new_skill)
    }), 201


@token_required
def get_skill_by_id(skill_id):
    skill = SkillService.get_skill_by_id(skill_id)
    return jsonify({
        "message": "Skill retrieved successfully",
        "skill": skill_schema.dump(skill)
    }), 200

@token_required
def get_skill_by_name(name):
    skill = SkillService.get_skill_by_name(name)
    return jsonify({
        "message": "Skill retrieved successfully",
        "skill": skill_schema.dump(skill)
    }), 200

@admin_required
def update_skill(skill_id):
    try:
        skill_data = skill_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    updated_skill = SkillService.update_skill(skill_id, skill_data)
    return jsonify({
        "message": "Skill updated successfully",
        "skill": skill_schema.dump(updated_skill)
    }), 200

@admin_required
def delete_skill(skill_id):
    SkillService.delete_skill(skill_id)
    return jsonify({"message": "Skill deleted successfully"}), 200

@token_required
def get_all_skills():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_skills = SkillService.get_all_skills()
    return jsonify({
        "message": "Skills retrieved successfully",
        "skills": skill_schema.dump(all_skills, many=True)
    }), 200

@token_required
def get_neighbors_by_skill(skill_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = SkillService.get_neighbors_by_skill(skill_id)
    return jsonify({
        "message": "Neighbors by skill retrieved successfully",
        "neighbors": neighbors_schema.dump(all_neighbors, many=True)
    }), 200

@token_required
def remove_skill_from_neighbor(neighbor_id, skill_id):
    if neighbor_id != get_current_user():
        return jsonify({"error": "You are not the owner of this account"}), 403
    if not neighbor_id:
        return jsonify({"error": "Neighbor not found"}), 404
    SkillService.remove_skill_from_neighbor(neighbor_id, skill_id)
    return jsonify({"message": "Skill removed from neighbor successfully"}), 200

@token_required
def add_skill_to_neighbor(neighbor_id, skill_id):
    if neighbor_id != get_current_user():
        return jsonify({"error": "You are not the owner of this account"}), 403
    SkillService.add_skill_to_neighbor(neighbor_id, skill_id)
    return jsonify({"message": "Skill added to neighbor successfully"}), 200




