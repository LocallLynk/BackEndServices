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
for category, skills in skill_bank.items():
    print(f"{category}:")
    for skill in skills:
        print(f"  - {skill}")

if skill != skill_bank:
    print("Skill not found. Would you like to add it to the skill bank? (y/n): ").lower()
    if input == "y":
        create_skill(skill_data)
    else:
        print("Skill not added.")