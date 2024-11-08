from database import db, Base
from models.skill import Skill
from models.neighbor import Neighbor
from sqlalchemy import select
from sqlalchemy.orm import Session

def populate_skill_bank(db_session: Session):
    for category, skills in skill_bank.items():
        for skill_name in skills:
            
            existing_skill = db_session.query(Skill).filter_by(name=skill_name).first()
            if existing_skill:
                continue

            new_skill = Skill(
                name=skill_name,
                experience="Beginner",  # Default experience level; adjust as needed
                description=f"{skill_name} skill under {category} category.",
                
            )

            db_session.add(new_skill)

    db_session.commit()
    print("Skill bank has been populated.")

def create_skill(skill_data):
    new_skill = Skill(
        name=skill_data['name'],
        experience=skill_data['experience'],
        description=skill_data['description']
    )

    db.session.add(new_skill)
    db.session.commit()
    db.session.refresh(new_skill)

    return new_skill
# def add_skill_to_neighbor(neighbor_id, skill_id):
#     neighbor = db.session.get(Neighbor, neighbor_id)
#     skill = db.session.get(Skill, skill_id)

#     if not neighbor:
#         print("Neighbor not found.")
#         return None
#     if not skill:
#         print("Skill not found.")
#         return None

#     neighbor.skills.append(skill)
#     db.session.commit()
#     db.session.refresh(neighbor)
#     print("Skill added successfully.")
    
#     return neighbor

def find_skill_by_name(skill_name):
    query = select(Skill).where(Skill.name == skill_name)
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
    return skill_bank.get(category)

def get_all_skills():
    return skill_bank

def get_skill_by_id(skill_id):
    skill = db.session.get(Skill, skill_id)
    if skill is None:
        raise ValueError("Skill not found.")
    return skill

def update_skill(skill_id, skill_data):
    skill = db.session.get(Skill, skill_id)
    if not skill:
        raise ValueError("Skill not found.")
    
    skill.name = skill_data.get('skill_name', skill.name)
    skill.description = skill_data.get('skill_description', skill.description)
    skill.experience = skill_data.get('skill_experience', skill.experience)
    db.session.commit()
    db.session.refresh(skill)
    
    return skill

def delete_skill(skill_id, confirm_deletion):
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
    
    query = select(Neighbor).where(Neighbor.skills.any(Skill.id == skill_id))
    result = db.session.execute(query)
    return result.scalars().all()

def get_skills_by_neighbor(neighbor_id):
   
    query = select(Skill).where(Skill.neighbors.any(Neighbor.id == neighbor_id))
    result = db.session.execute(query)
    return result.scalars().all()

def remove_skill_from_neighbor(neighbor_id, skill_id):
    
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
