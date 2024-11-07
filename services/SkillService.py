from database import db
from models.neighbor import Neighbor
from models.skill import Skill
from sqlalchemy import select

def create_skill(skill_data):
    """Creates a new skill and saves it to the database."""
    new_skill = Skill(
        skill_name=skill_data['skill_name'], 
        skill_description=skill_data['skill_description'],
        skill_experience=skill_data['skill_experience']
    )
    
    db.session.add(new_skill)
    db.session.commit()
    db.session.refresh(new_skill)  # Refresh to retrieve the new skill ID
    
    return new_skill

def add_skill_to_neighbor(neighbor_id, skill_id):
    """Adds a skill to a neighbor's profile."""
    neighbor = db.session.get(Neighbor, neighbor_id)
    skill = db.session.get(Skill, skill_id)

    if not neighbor:
        print("Neighbor not found.")
        return None
    if not skill:
        print("Skill not found.")
        return None

    neighbor.skills.append(skill)
    db.session.commit()
    db.session.refresh(neighbor)
    print("Skill added successfully.")
    
    return neighbor

def find_skill_by_name(skill_name):
    """Finds a skill by name."""
    query = select(Skill).where(Skill.skill_name == skill_name)
    result = db.session.execute(query)
    return result.scalars().first()

# Predefined skill categories and skills
skill_bank = {
    "Technology": [
        "Python Programming", "Data Science", "Web Development", "Cybersecurity",
        "Machine Learning", "Blockchain Technology", "Cloud Computing",
        "Mobile App Development", "Artificial Intelligence"
    ],
    "Creative Arts": [
        "Graphic Design", "Illustration", "Digital Art", "Photography",
        "Videography", "Music Production", "3D Modeling", "Animation",
        "Creative Writing"
    ],
    "Business": [
        "Entrepreneurship",
        "Marketing Strategy",
        "Project Management",
        "Accounting",
        "Leadership Skills",
        "E-commerce",
        "Sales Techniques",
        "SEO Optimization",
        "Financial Analysis"
    ],
    "Personal Development": [
        "Public Speaking",
        "Time Management",
        "Stress Management",
        "Goal Setting",
        "Emotional Intelligence",
        "Mindfulness Meditation",
        "Resilience Building",
        "Career Coaching",
        "Self-Discipline"
    ],
    "Language Learning": [
        "English",
        "Spanish",
        "Mandarin Chinese",
        "French",
        "German",
        "Japanese",
        "Italian",
        "Russian",
        "Arabic"
    ],
    "Health & Fitness": [
        "Yoga",
        "Pilates",
        "Strength Training",
        "Nutrition",
        "Weight Loss Coaching",
        "Personal Training",
        "Mindfulness Meditation",
        "Sleep Optimization",
        "Mental Health Support"
    ],
    "Lifestyle": [
        "Cooking",
        "Gardening",
        "Travel Planning",
        "Interior Design",
        "Minimalism",
        "Fashion Styling",
        "Pet Care",
        "DIY Crafts",
        "Event Planning"
    ],
    "Education & Teaching": [
        "Tutoring (Math, Science, etc.)",
        "Curriculum Development",
        "Online Teaching",
        "Special Needs Education",
        "Instructional Design",
        "Education Technology",
        "ESL Teaching",
        "Early Childhood Education",
        "Test Prep Coaching"
    ]
    # More categories can be added as needed
}

def get_skills_by_category(category):
    """Retrieves skills for a specific category from the skill bank."""
    return skill_bank.get(category)

def get_all_skills():
    """Returns all skills organized by category."""
    return skill_bank

def get_skill_by_id(skill_id):
    """Finds a skill by its ID."""
    skill = db.session.get(Skill, skill_id)
    if skill is None:
        raise ValueError("Skill not found.")
    return skill

def update_skill(skill_id, skill_data):
    """Updates an existing skill's information."""
    skill = db.session.get(Skill, skill_id)
    if not skill:
        raise ValueError("Skill not found.")

    skill.skill_name = skill_data.get('skill_name', skill.skill_name)
    skill.skill_description = skill_data.get('skill_description', skill.skill_description)
    skill.skill_experience = skill_data.get('skill_experience', skill.skill_experience)
    db.session.commit()
    db.session.refresh(skill)
    
    return skill

def delete_skill(skill_id, confirm_deletion):
    """Deletes a skill if confirmed by user."""
    skill = db.session.get(Skill, skill_id)
    if not skill:
        raise ValueError("Skill not found.")

    if confirm_deletion.lower() == 'y':
        db.session.delete(skill)
        db.session.commit()
        print("Skill deleted.")
        return skill
    else:
        print("Skill deletion cancelled.")
        return None

def get_neighbors_by_skill(skill_id):
    """Retrieves neighbors associated with a specific skill ID."""
    query = select(Neighbor).where(Neighbor.skills.any(Skill.id == skill_id))
    result = db.session.execute(query)
    return result.scalars().all()

def get_skills_by_neighbor(neighbor_id):
    """Retrieves skills associated with a specific neighbor ID."""
    query = select(Skill).where(Skill.neighbors.any(Neighbor.id == neighbor_id))
    result = db.session.execute(query)
    return result.scalars().all()

def remove_skill_from_neighbor(neighbor_id, skill_id):
    """Removes a skill from a neighbor."""
    neighbor = db.session.get(Neighbor, neighbor_id)
    skill = db.session.get(Skill, skill_id)

    if not neighbor:
        print("Neighbor not found.")
        return None
    if not skill:
        print("Skill not found.")
        return None

    if skill in neighbor.skills:
        neighbor.skills.remove(skill)
        db.session.commit()
        db.session.refresh(neighbor)
        print("Skill removed successfully.")
    else:
        print("Skill is not associated with this neighbor.")
    
    return neighbor
