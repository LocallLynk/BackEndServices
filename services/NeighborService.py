from database import db, Base  # services interact directly with the db
from models import Neighbor, Skill, Task
from models.post import Post
from models.schema import postSchema, taskSchema
from sqlalchemy import select
from utils.util import encode_role_token
from datetime import date
import hashlib
import secrets
from flask import request, redirect, url_for

def generate_password_hash(password):
   
    salt = secrets.token_bytes(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password, salt

def verify_password(password, hashed_password, salt):
    
    test_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return test_hash == hashed_password

# Creating a new neighbor
def create_neighbor(neighbor_data):
    password_hash, salt = generate_password_hash(neighbor_data['password'])
    
    skills = []
    
    if 'skills' in neighbor_data:
        skill_ids = neighbor_data['skills']  
        skills = db.session.query(Skill).filter(Skill.id.in_(skill_ids)).all()
    # Set a default profile picture URL if none is provided
    default_profile_pic = 'https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png'
    
    new_neighbor = Neighbor(
        first_name=neighbor_data['first_name'],
        last_name=neighbor_data['last_name'], 
        email=neighbor_data['email'],
        phone=neighbor_data['phone'], 
        zipcode=neighbor_data['zipcode'],
        username=neighbor_data['username'], 
        password=password_hash, 
        salt=salt,
        skills=[],
        admin=neighbor_data['admin'],
        profile_pic=neighbor_data.get('profile_pic', default_profile_pic) or default_profile_pic)

    
    
    db.session.add(new_neighbor)
    db.session.commit()
    db.session.refresh(new_neighbor)
    return new_neighbor

def make_admin(neighbor_id):
    neighbor = db.session.get(Neighbor, neighbor_id)
    if not neighbor:
        print("Neighbor not found")
        return None

    neighbor.admin = True
    db.session.commit()
    db.session.refresh(neighbor)
    print("Neighbor is now an admin")
    return neighbor

def remove_admin(neighbor_id):
    neighbor = db.session.get(Neighbor, neighbor_id)
    if not neighbor:
        print("Neighbor not found")
        return None

    neighbor.admin = False
    db.session.flush()
    db.session.commit()
    db.session.refresh(neighbor)
    print("Neighbor is no longer an admin")
    return neighbor
#-------- Searching for neighbors --------

def get_all_neighbors(page=1, per_page=20):
    query = select(Neighbor).order_by(Neighbor.zipcode).limit(per_page).offset((page - 1) * per_page)
    result = db.session.execute(query)
    return result.scalars().all()

def get_neighbor_by_id(neighbor_id):
    query = select(Neighbor).where(Neighbor.id == neighbor_id)
    result = db.session.execute(query).one_or_none()
    neighbor = result
    if not neighbor:
        raise ValueError("Neighbor not found.")
    return neighbor

def get_neighbor_by_username(username):
    query = select(Neighbor).where(Neighbor.username == username)
    result = db.session.execute(query).one_or_none()
    neighbor = result.scalars()
    if not neighbor:
        raise ValueError("Neighbor not found.")
    return neighbor

def get_neighbor_by_email(email):
    query = select(Neighbor).where(Neighbor.email == email)
    result = db.session.execute(query).one_or_none()
    neighbor = result.scalars()
    if not neighbor:
        raise ValueError("Neighbor not found.")
    return neighbor

def get_neighbor_by_zipcode(zipcode):
    query = select(Neighbor).where(Neighbor.zipcode == zipcode)
    result = db.session.execute(query)
    return result.scalars().all()
    


#-------- Logging in --------


def validate_user(email):
    # Query the database to check if the email exists
    user = Neighbor.query.filter_by(email=Neighbor.email).first()

    if user:
        # If the email exists, redirect to their homepage
        return redirect(url_for('home_feed', neighbor_id=user.id))
    else:
        # If the email does not exist, redirect to the account creation page
        return redirect(url_for('create_neighbor'))


def login(credentials):
    query = select(Neighbor).where(Neighbor.email == credentials['email'])
    neighbor = db.session.execute(query).scalar_one_or_none()
    password = credentials['password'] 

    if neighbor and verify_password(password, neighbor.password, neighbor.salt):
        print(f'Login successful. Welcome, {neighbor.first_name}')
        return encode_role_token(neighbor.id, 'neighbor')
    else:
        print('Invalid username or password')
        return None

#-------- Updating a neighbor's information --------

@staticmethod
def get_home_feed(user_id):
    
    # Example queries: Fetch posts and tasks for the feed
    posts = Post.query.order_by(Post.created_on.desc()).limit(20).all()  # Latest 20 posts
    tasks = Task.query.filter(Task.task_neighbor_id == user_id).limit(20).all()  # User-specific tasks

    # Convert data to JSON-friendly format
    post_data = [postSchema.dump(post) for post in posts]
    task_data = [taskSchema.dump(task) for task in tasks]

    # Return the structured feed data
    return {
        "posts": post_data,
        "tasks": task_data
    }

def update_neighbor(neighbor_id, neighbor_data):
    neighbor = db.session.execute(select(Neighbor).where(Neighbor.id == neighbor_id)).scalar()
    
    if not neighbor:
        print("Neighbor not found")
        return None
    neighbor.profile_pic = neighbor_data.get('profile_pic', neighbor.profile_pic)
    neighbor.first_name = neighbor_data.get('first_name', neighbor.first_name)
    neighbor.last_name = neighbor_data.get('last_name', neighbor.last_name)
    neighbor.email = neighbor_data.get('email', neighbor.email)
    neighbor.phone = neighbor_data.get('phone', neighbor.phone)
    neighbor.zipcode = neighbor_data.get('zipcode', neighbor.zipcode)
    neighbor.username = neighbor_data.get('username', neighbor.username)
    neighbor.admin = neighbor_data.get('admin', neighbor.admin)

    if 'password' in neighbor_data:
        neighbor.password, neighbor.salt = generate_password_hash(neighbor_data['password'])

    db.session.commit()
    db.session.refresh(neighbor)
    print("Changes updated successfully")
    return neighbor

#-------- Deleting a neighbor --------

def delete_neighbor(neighbor_id):
    neighbor = db.session.get(Neighbor, neighbor_id)
    if not neighbor:
        print("Neighbor not found")
        return None

    db.session.delete(neighbor)
    db.session.commit()
    print("Neighbor deleted")



