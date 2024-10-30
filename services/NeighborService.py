from database import db #services interact directly with the db
from models.neighbor import Neighbor #need this to create customer objects
from sqlalchemy import select #so we can query our db
from utils.util import encode_role_token
from models.task import Task
from sqlalchemy import select #so we can query our db
from models.skill import Skill
from models.feedback import Feedback
from datetime import date

#Creating a new neighbor

def create_neighbor(neighbor_data):
    new_neighbor = Neighbor(name=neighbor_data['name'], email=neighbor_data['email'], 
                   phone=neighbor_data['phone'], zipcode=neighbor_data['zipcode'], 
                   username=neighbor_data['username'], password=neighbor_data['password'], 
                   overall_rating=0, num_ratings=0, num_rated=0, created_on=date.today())
    
    db.session.add(new_neighbor)
    db.session.commit() #adding the new neighbor to the db

    db.session.refresh(new_neighbor) #refreshing the db to get the new neighbor's id

    return new_neighbor

#--------Searching for neighbors--------

def get_all_neighbors(page=1, per_page=10):
    query = select(Neighbor).order_by(Neighbor.zipcode).limit(per_page).offset((page - 1) * per_page)
    result = db.session.execute(query)
    all_neighbors = result.scalars().all()

    return all_neighbors

def get_neighbor_by_id(neighbor_id):
    query = select(Neighbor).where(Neighbor.id == neighbor_id)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    return neighbor

def get_neighbor_by_username(username):
    query = select(Neighbor).where(Neighbor.username == username)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    return neighbor

def get_neighbor_by_email(email):
    query = select(Neighbor).where(Neighbor.email == email)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    return neighbor

def get_neighbor_by_zipcode(zipcode):
    query = select(Neighbor).where(Neighbor.zipcode == zipcode)
    result = db.session.execute(query)
    neighbors = result.scalars().all()

    return neighbors

def get_neighbor_by_skill(skill_id):
    query = select(Neighbor).join(Skill).where(Skill.id == skill_id)
    result = db.session.execute(query)
    neighbors = result.scalars().all()

    return neighbors

def get_neighbor_by_task(task_id):
    query = select(Neighbor).join(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    neighbor = result.scalars().all()

    return neighbor

def get_neighbor_by_feedback(feedback_id):
    query = select(Neighbor).join(Feedback).where(Feedback.id == feedback_id)
    result = db.session.execute(query)
    neighbor = result.scalars().all()

    return neighbor

def get_neighbor_by_rating(rating):
    query = select(Neighbor).where(Neighbor.overall_rating == rating)
    result = db.session.execute(query)
    neighbors = result.scalars().all()

    return neighbors

#--------Logging in--------

def login(username, password):
    query = select(Neighbor).where(Neighbor.username == username).where(Neighbor.password == password)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    if neighbor:
        print(f'Login successful', 'Welcome', {neighbor.name})
        return encode_role_token(neighbor.id, 'neighbor')
    else:
        print('Invalid username or password')
        return None
    
#--------Updating a neighbor's information--------

def update_neighbor(neighbor_id, neighbor_data):
    query = select(Neighbor).where(Neighbor.id == neighbor_id)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    if neighbor:
        neighbor.name = neighbor_data['name']
        neighbor.email = neighbor_data['email']
        neighbor.phone = neighbor_data['phone']
        neighbor.zipcode = neighbor_data['zipcode']
        neighbor.username = neighbor_data['username']
        neighbor.password = neighbor_data['password']

        db.session.commit()
        db.session.refresh(neighbor)
        print('Changes updated successfully')
        return neighbor
    else:
        print('Neighbor not found')
        return None
    

#--------Deleting a neighbor--------

def delete_neighbor(neighbor_id):
    query = select(Neighbor).where(Neighbor.id == neighbor_id)
    result = db.session.execute(query)
    neighbor = result.scalars().first()

    if neighbor:
        input('Are you sure you want to delete your account? This cannot be undone. Press Y to confirm.')
        if input == 'Y':
            db.session.delete(neighbor)
            db.session.commit()
            print('Account deleted successfully')

            return neighbor
        else:
            print('Account deletion cancelled')
            return None
    else:
        print('Account not found')
        return None
    

