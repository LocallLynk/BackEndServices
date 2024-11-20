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
                category=f"{category}",
                experience="Beginner",  # Default experience level; adjust as needed
                description=f"{skill_name} skill."  # Default description; adjust as needed
                
            )

            db_session.add(new_skill)

    db_session.commit()
    print("Skill bank has been populated.")

def create_skill(skill_data):
    new_skill = Skill(
        name=skill_data['name'],
        category=skill_data['category'],
        experience=skill_data['experience'],
        description=skill_data['description']
    )

    db.session.add(new_skill)
    db.session.commit()
    db.session.refresh(new_skill)

    return new_skill

def add_skill_to_neighbor(neighbor_id, skill_id):
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

def get_skill_by_name(name):
    name = name.capitalize()
    query = select(Skill).where(Skill.name == name)
    result = db.session.execute(query)
    return result.scalars().first()

# Predefined skill categories and skills
skill_bank = { 
    "Technical Skills": [
        "Python", "JavaScript", "Java", "C#", "C++", "Ruby", "Go", "PHP", "Swift", "Kotlin", "R", "SQL", "NoSQL", 
        "HTML", "CSS", "React", "Angular", "Vue.js", "Node.js", "Express.js", "Django", "Flask", "Spring Boot", 
        "ASP.NET", "Ruby on Rails", "GraphQL", "REST APIs", "Docker", "Kubernetes", "AWS", "Azure", "Google Cloud", 
        "Linux", "Unix", "Git", "GitHub", "GitLab", "Jenkins", "CI/CD", "Jira", "Azure DevOps", "Terraform", "Ansible", 
        "Nginx", "Apache", "MySQL", "PostgreSQL", "MongoDB", "Redis", "SQLite", "MariaDB", "Elasticsearch", 
        "Solr", "RabbitMQ", "Kafka", "TensorFlow", "PyTorch", "OpenCV", "Machine Learning", "Deep Learning", 
        "Natural Language Processing", "Computer Vision", "AI", "Data Science", "Data Analysis", "Data Visualization", 
        "Statistics", "Mathematics", "Big Data", "Hadoop", "Spark", "Tableau", "Power BI", "Excel", "Google Analytics", 
        "Google Tag Manager", "SEO", "SEM", "Content Management System", "WordPress", "Drupal", "Magento", "Shopify", 
        "Adobe Photoshop", "Adobe Illustrator", "Figma", "Sketch", "InVision", "UI/UX Design", "Wireframing", "Prototyping", 
        "Agile", "Scrum", "Kanban", "DevOps", "Automated Testing", "Unit Testing", "Integration Testing", "TDD", "BDD", 
        "Selenium", "Jest", "Mocha", "JUnit", "PyTest", "Cypress", "Postman", "Swagger", "OAuth", "JWT", "Graph Databases"
    ],
    "Business Skills": [
        "Project Management", "Leadership", "Communication", "Negotiation", "Strategic Planning", "Problem Solving", 
        "Team Management", "Budgeting", "Time Management", "Risk Management", "Supply Chain Management", "Change Management", 
        "Business Analysis", "Client Relations", "Sales", "Marketing", "Financial Modeling", "Sales Forecasting", 
        "Customer Service", "Event Planning", "Product Management", "Operations Management", "Market Research", "Branding", 
        "Public Relations", "Business Development", "Customer Retention", "Vendor Management", "Compliance", "Contract Management", 
        "Legal Knowledge", "Fundraising", "Mergers & Acquisitions", "Investor Relations", "Crisis Management", "Cultural Sensitivity", 
        "Human Resources", "Recruitment", "Onboarding", "Employee Engagement", "Training and Development", "Compensation & Benefits", 
        "Performance Management", "Employee Relations", "Payroll", "Labor Laws", "Workplace Diversity", "Organizational Development", 
        "Team Building", "Networking", "Conflict Resolution", "Staff Scheduling", "Talent Acquisition", "Internship Program Management"
    ],
    "Creative Skills": [
        "Graphic Design", "Illustration", "Photography", "Videography", "Animation", "Video Editing", "3D Modeling", 
        "Motion Graphics", "UI/UX Design", "Product Design", "Fashion Design", "Interior Design", "Web Design", "App Design", 
        "Art Direction", "Brand Identity", "Packaging Design", "Typography", "Logo Design", "Color Theory", "Photo Editing", 
        "Concept Art", "Storyboard Creation", "Cinematography", "Film Production", "Content Creation", "Social Media Marketing", 
        "Content Writing", "Blogging", "Copywriting", "Journalism", "Public Speaking", "Podcasting", "Music Production", 
        "Sound Editing", "Voice Acting", "Stage Design", "Scriptwriting", "Storytelling", "Creative Writing", "Poetry", 
        "Playwriting", "Literary Criticism", "Book Editing", "Publishing", "Transmedia Storytelling", "Radio Broadcasting", 
        "TV Production", "Digital Art", "Photography Editing", "Video Storytelling", "Content Strategy", "Brand Storytelling", 
        "Film Editing", "Creative Project Management", "Art Curation", "Gallery Management", "Event Design"
    ],
    "Soft Skills": [
        "Emotional Intelligence", "Teamwork", "Adaptability", "Work Ethic", "Critical Thinking", "Problem Solving", 
        "Creativity", "Decision Making", "Self-motivation", "Stress Management", "Active Listening", "Empathy", "Confidence", 
        "Patience", "Resilience", "Collaboration", "Initiative", "Self-discipline", "Time Management", "Open-mindedness", 
        "Presentation Skills", "Conflict Resolution", "Negotiation", "Customer Focus", "Networking", "Mentoring", 
        "Coaching", "Interpersonal Skills", "Self-awareness", "Delegation", "Learning Agility", "Cultural Sensitivity", 
        "Relationship Building", "Persuasion", "Listening Skills", "Positive Attitude", "Assertiveness", "Trustworthiness", 
        "Leadership", "Work-life Balance", "Decision Making", "Goal Setting", "Stress Reduction"
    ],
    "Sales & Marketing Skills": [
        "Sales Strategy", "Lead Generation", "Market Research", "Customer Acquisition", "Product Marketing", "Brand Strategy", 
        "Digital Marketing", "Email Marketing", "SEO", "SEM", "PPC", "Google Ads", "Facebook Ads", "Affiliate Marketing", 
        "Influencer Marketing", "Social Media Strategy", "Content Marketing", "Video Marketing", "Mobile Marketing", 
        "Public Relations", "Event Marketing", "Market Segmentation", "Competitive Analysis", "CRM", "Sales Forecasting", 
        "Sales Presentations", "Account Management", "B2B Sales", "B2C Sales", "Retail Marketing", "Customer Retention", 
        "Product Launch", "Trade Shows", "Sales Process Optimization", "Telemarketing", "E-commerce Marketing", "Product Pricing", 
        "Campaign Management", "Product Positioning", "Target Market Analysis", "Branding", "Viral Marketing", "Negotiation"
    ],
    "Management Skills": [
        "Project Management", "People Management", "Team Leadership", "Resource Allocation", "Budget Management", 
        "Risk Management", "Strategic Planning", "Delegation", "Organizational Skills", "Coaching", "Change Management", 
        "Conflict Management", "Decision Making", "Operations Management", "Crisis Management", "Time Management", 
        "Productivity Optimization", "Process Improvement", "Decision Making", "Employee Engagement", "Motivation", 
        "Team Development", "Business Planning", "Financial Planning", "Staffing", "Performance Evaluation", 
        "Client Management", "Vendor Management", "Policy Development", "Compliance Management", "Workforce Planning", 
        "Change Leadership", "Training & Development", "Workplace Culture", "Workforce Optimization", "Remote Team Management"
    ],
    "Finance Skills": [
        "Financial Modeling", "Budgeting", "Accounting", "Financial Planning", "Financial Analysis", "Bookkeeping", 
        "Investment Analysis", "Risk Management", "Taxation", "Asset Management", "Portfolio Management", "Corporate Finance", 
        "Mergers & Acquisitions", "Venture Capital", "Private Equity", "Financial Reporting", "Forensic Accounting", 
        "Cash Flow Management", "Banking", "Financial Auditing", "Financial Risk Assessment", "Corporate Tax Planning", 
        "Wealth Management", "Insurance", "Financial Forecasting", "Business Valuation", "Credit Analysis", "Loan Structuring", 
        "Debt Management", "Stock Market Analysis", "Real Estate Investment", "Financial Modeling in Excel", "Fundraising"
    ],
    "Healthcare Skills": [
        "Medical Coding", "Medical Billing", "Nursing", "Pharmacy", "Physical Therapy", "Patient Care", "Healthcare Administration", 
        "Healthcare Management", "Clinical Research", "Medical Transcription", "Emergency Medical Services", "Surgical Assistance", 
        "Radiology", "Anesthesia", "Geriatrics", "Orthopedics", "Family Medicine", "Psychiatry", "Dentistry", "Laboratory Skills", 
        "Emergency Room Care", "Pediatric Care", "Nutritional Counseling", "Health Education", "Telemedicine", "Infectious Diseases", 
        "Medical Records", "Healthcare IT", "Health Insurance", "Pharmaceuticals", "Health Advocacy", "Surgical Preparation", 
        "Medical Research", "Patient Advocacy", "Health Policy", "Triage", "Diagnostic Testing", "Medical Sales"
    ]
}

def get_skills_by_category(category):
    return skill_bank.get(category)

def get_all_skills():
    query = select(Skill)
    result = db.session.execute(query)
    return result.scalars().all()

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
    skill.category = skill_data.get('skill_category', skill.category)
    skill.description = skill_data.get('skill_description', skill.description)
    skill.experience = skill_data.get('skill_experience', skill.experience)
    db.session.commit()
    db.session.refresh(skill)
    
    return skill

def delete_skill(skill_id):
    skill = db.session.get(Skill, skill_id)
    if not skill:
        raise ValueError("Skill not found.")

    else:
        db.session.delete(skill)
        db.session.commit()
        print("Skill deleted.")
        return skill
   

def get_neighbors_by_skill(skill_id):
    
    query = select(Neighbor).where(Neighbor.skills.any(Skill.id == skill_id))
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

