from database import db #services interact directly with the db
from models.neighbor import Neighbor
from sqlalchemy import select #so we can query our db
from models.feedback import Feedback
from datetime import date
from models.skill import Skill

def create_skill(skill_data):
    new_skill = Skill(skill_name=skill_data['skill_name'], 
                skill_description=skill_data['skill_description'],
                skill_experience=skill_data['skill_experience'])
    
    db.session.add(new_skill)
    db.session.commit() #adding the new skill to the db

    db.session.refresh(new_skill) #refreshing the db to get the new skill's id

    return new_skill

def find_skill_by_name(skill_name):
    query = select(Skill).where(Skill.skill_name == skill_name)
    result = db.session.execute(query)
    skill = result.scalars().first()

    return skill

skill_bank = {
    "Technology": [
        "Python Programming",
        "Data Science",
        "Web Development",
        "Cybersecurity",
        "Machine Learning",
        "Blockchain Technology",
        "Cloud Computing",
        "Mobile App Development",
        "Artificial Intelligence"
    ],
    "Creative Arts": [
        "Graphic Design",
        "Illustration",
        "Digital Art",
        "Photography",
        "Videography",
        "Music Production",
        "3D Modeling",
        "Animation",
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
}

# Example usage

def get_all_skills():
    for category, skills in skill_bank.items():
        print(f"{category}:")
    for skill in skills:
        print(f"  - {skill}")
    return skill_bank

def get_skill_by_id(skill_id):
    query = select(Skill).where(Skill.id == skill_id)
    result = db.session.execute(query)
    skill = result.scalars().first()

    return skill

def get_skill_by_name(skill_name):
    query = select(Skill).where(Skill.skill_name == skill_name)
    result = db.session.execute(query)
    skill = result.scalars().first()

    return skill

def update_skill(skill_id, skill_data):
    query = select(Skill).where(Skill.id == skill_id)
    result = db.session.execute(query)
    skill = result.scalars().first()

    skill.skill_name = skill_data['skill_name']
    skill.skill_description = skill_data['skill_description']
    skill.skill_experience = skill_data['skill_experience']
    db.session.commit()

    return skill

def delete_skill(skill_id):
    query = select(Skill).where(Skill.id == skill_id)
    result = db.session.execute(query)
    skill = result.scalars().first()
    input("Are you sure you want to delete this skill? (y/n): ").lower()
    if input == "y":
        db.session.delete(skill)
        db.session.commit()
        print("Skill deleted.")
        return skill
    else:
        print("Skill deletion cancelled")
        return None
    
def get_neighbors_by_skill(skill_id):
    query = select(Neighbor).where(Neighbor.skills.any(Skill.id == skill_id))
    result = db.session.execute(query)
    neighbors = result.scalars().all()

    return neighbors

def get_skills_by_neighbor(neighbor_id):
    query = select(Skill).where(Skill.neighbors.any(Neighbor.id == neighbor_id))
    result = db.session.execute(query)
    skills = result.scalars().all()

    return skills

def remove_skill_from_neighbor(neighbor_id, skill_id):
    query = select(Neighbor).where(Neighbor.id == neighbor_id)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    query = select(Skill).where(Skill.id == skill_id)
    result = db.session.execute(query)
    skill = result.scalars().first()

    if neighbor and skill:
        neighbor.skills.remove(skill)
        db.session.commit()
        db.session.refresh(neighbor)
        print('Skill removed successfully')
    else:
        print('Neighbor or skill not found')

    return neighbor