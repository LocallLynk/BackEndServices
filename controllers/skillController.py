from flask import request, jsonify
from models.schemas.skillSchema import skill_schema
from models.schemas.neighborSchema import neighbor_schema
from services import SkillService
from marshmallow import ValidationError
from utils.util import token_required, admin_required

@token_required
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
    skill = SkillService.find_skill_by_id(skill_id)
    return jsonify({
        "message": "Skill retrieved successfully",
        "skill": skill_schema.dump(skill)
    }), 200

@token_required
def get_skill_by_name(skill_name):
    skill = SkillService.find_skill_by_name(skill_name)
    return jsonify({
        "message": "Skill retrieved successfully",
        "skill": skill_schema.dump(skill)
    }), 200

@admin_required
def update_skill(current_skill):
    try:
        skill_data = skill_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    updated_skill = SkillService.update_skill(current_skill, skill_data)
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

    all_skills = SkillService.get_all_skills(page, per_page)
    return jsonify({
        "message": "Skills retrieved successfully",
        "skills": skill_schema.dump(all_skills, many=True)
    }), 200

@token_required
def get_skill_by_neighbor_id(neighbor_id):
    skill = SkillService.find_skill_by_neighbor_id(neighbor_id)
    return jsonify({
        "message": "Skill by neighbor ID retrieved successfully",
        "skill": skill_schema.dump(skill)
    }), 200

@token_required
def get_skill_by_zipcode(zipcode):
    skill = SkillService.find_skill_by_zipcode(zipcode)
    return jsonify({
        "message": "Skill by zipcode retrieved successfully",
        "skill": skill_schema.dump(skill)
    }), 200

@token_required
def get_neighbors_by_skill(skill_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    all_neighbors = SkillService.get_neighbor_by_skill(skill_id, page, per_page)
    return jsonify({
        "message": "Neighbors by skill retrieved successfully",
        "neighbors": neighbors_schema.dump(all_neighbors, many=True)
    }), 200

@token_required
def remove_skill_from_neighbor(neighbor_id, skill_id):
    SkillService.remove_skill_from_neighbor(neighbor_id, skill_id)
    return jsonify({"message": "Skill removed from neighbor successfully"}), 200

@token_required
def add_skill_to_neighbor(neighbor_id, skill_id):
    SkillService.add_skill_to_neighbor(neighbor_id, skill_id)
    return jsonify({"message": "Skill added to neighbor successfully"}), 200




