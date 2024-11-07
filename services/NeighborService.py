from database import db, Base  # services interact directly with the db
from models import Neighbor, Skill, Task, Feedback
from sqlalchemy import select
from utils.util import encode_role_token
from datetime import date
import hashlib
import secrets

def generate_password_hash(password):
    """Generates a secure password hash using the Argon2 algorithm."""
    salt = secrets.token_bytes(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password, salt

def verify_password(password, hashed_password, salt):
    """Verifies a password against a stored hash and salt."""
    test_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return test_hash == hashed_password

# Creating a new neighbor
def create_neighbor(neighbor_data):
    password_hash, salt = generate_password_hash(neighbor_data['password'])
    new_neighbor = Neighbor(
        name=neighbor_data['name'], 
        email=neighbor_data['email'],
        phone=neighbor_data['phone'], 
        zipcode=neighbor_data['zipcode'],
        username=neighbor_data['username'], 
        password=password_hash, 
        salt=salt,
        overall_rating=0, 
        num_ratings=0, 
        num_rated=0,
        skills=[], 
        admin=0, 
        created_on=date.today()
    )
    
    db.session.add(new_neighbor)
    db.session.commit()
    db.session.refresh(new_neighbor)
    return new_neighbor

#-------- Searching for neighbors --------

def get_all_neighbors(page=1, per_page=10):
    query = select(Neighbor).order_by(Neighbor.zipcode).limit(per_page).offset((page - 1) * per_page)
    result = db.session.execute(query)
    return result.scalars().all()

def get_neighbor_by_id(neighbor_id):
    neighbor = db.session.get(Neighbor, neighbor_id)
    if not neighbor:
        raise ValueError("Neighbor not found.")
    return neighbor

def get_neighbor_by_username(username):
    query = select(Neighbor).where(Neighbor.username == username)
    result = db.session.execute(query)
    neighbor = result.scalars().first()
    return neighbor

def get_neighbor_by_email(email):
    query = select(Neighbor).where(Neighbor.email == email)
    result = db.session.execute(query)
    return result.scalars().first()

def get_neighbor_by_zipcode(zipcode):
    query = select(Neighbor).where(Neighbor.zipcode == zipcode)
    result = db.session.execute(query)
    return result.scalars().all()

def get_neighbor_by_skill(skill_id):
    query = select(Neighbor).join(Skill).where(Skill.id == skill_id)
    result = db.session.execute(query)
    return result.scalars().all()

def get_neighbor_by_task(task_id):
    query = select(Neighbor).join(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    return result.scalars().all()

def get_neighbor_by_feedback(feedback_id):
    query = select(Neighbor).join(Feedback).where(Feedback.id == feedback_id)
    result = db.session.execute(query)
    return result.scalars().all()

def get_neighbor_by_rating(rating):
    query = select(Neighbor).where(Neighbor.overall_rating == rating)
    result = db.session.execute(query)
    return result.scalars().all()

#-------- Logging in --------

def login(username, password):
    query = select(Neighbor).where(Neighbor.username == username)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    if neighbor and verify_password(password, neighbor.password, neighbor.salt):
        print(f'Login successful. Welcome, {neighbor.name}')
        return encode_role_token(neighbor.id, 'neighbor')
    else:
        print('Invalid username or password')
        return None

#-------- Updating a neighbor's information --------

def update_neighbor(neighbor_id, neighbor_data):
    neighbor = db.session.get(Neighbor, neighbor_id)
    if not neighbor:
        print("Neighbor not found")
        return None

    neighbor.name = neighbor_data.get('name', neighbor.name)
    neighbor.email = neighbor_data.get('email', neighbor.email)
    neighbor.phone = neighbor_data.get('phone', neighbor.phone)
    neighbor.zipcode = neighbor_data.get('zipcode', neighbor.zipcode)
    neighbor.username = neighbor_data.get('username', neighbor.username)
    neighbor.skills = neighbor_data.get('skills', neighbor.skills)

    if 'password' in neighbor_data:
        neighbor.password, neighbor.salt = generate_password_hash(neighbor_data['password'])

    db.session.commit()
    db.session.refresh(neighbor)
    print("Changes updated successfully")
    return neighbor

#-------- Deleting a neighbor --------

def delete_neighbor(neighbor_id, confirm_deletion):
    neighbor = db.session.get(Neighbor, neighbor_id)
    if not neighbor:
        print("Account not found")
        return None

    if confirm_deletion.lower() == 'y':
        db.session.delete(neighbor)
        db.session.commit()
        print("Account deleted successfully")
        return neighbor
    else:
        print("Account deletion cancelled")
        return None

def add_skill_to_neighbor(neighbor_id, skill_id):
    neighbor = db.session.get(Neighbor, neighbor_id)
    skill = db.session.get(Skill, skill_id)
    
    if not neighbor:
        print("Neighbor not found.")
        return None
    if not skill:
        input("Skill not found.")
        return None

       

    neighbor.skills.append(skill)
    db.session.commit()
    db.session.refresh(neighbor)
    print("Skill added successfully")
    return neighbor
