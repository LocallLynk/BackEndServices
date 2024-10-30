from database import db #services interact directly with the db
from models.neighbor import Neighbor
from sqlalchemy import select #so we can query our db
from models.feedback import Feedback
from datetime import date
from models.skill import Skill

def create_task(task_data):
    new_task = Task(task_neighbor_id=task_data['task_neighbor_id'], 
               client_neighbor_id=task_data['client_neighbor_id'],
               title=task_data['title'], description=task_data['description'], 
               skill_id=task_data['skill_id'], status="open", task_paid=task_data['task_paid'],
               traded_task=task_data['traded_task'], created_on=date.today())
    
    db.session.add(new_task)
    db.session.commit() #adding the new task to the db

    db.session.refresh(new_task) #refreshing the db to get the new task's id

    return new_task

def find_tasks_by_task_id(task_id):
    query = select(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    task = result.scalars().first()

    return task

def find_tasks_by_task_neighbor_id(task_neighbor_id):
    query = select(Task).where(Task.task_neighbor_id == task_neighbor_id)
    result = db.session.execute(query)
    tasks = result.scalars().all()

    return tasks

def find_tasks_by_client_neighbor_id(client_neighbor_id):
    query = select(Task).where(Task.client_neighbor_id == client_neighbor_id)
    result = db.session.execute(query)
    tasks = result.scalars().all()

    return tasks

def update_task_status(task_id, new_status):
    query = select(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    task = result.scalars().first()

    task.status = new_status
    db.session.commit()

    return task

def update_task_paid(task_id, task_paid):
    query = select(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    task = result.scalars().first()

    task.task_paid = task_paid
    db.session.commit()

    return task

def update_traded_task(task_id, traded_task):
    query = select(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    task = result.scalars().first()

    task.traded_task = traded_task
    db.session.commit()

    return task

def update_task(task_id, task_data):
    query = select(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    task = result.scalars().first()

    task.title = task_data['title']
    task.description = task_data['description']
    task.skill_id = task_data['skill_id']
    db.session.commit()

    return task

def delete_task(task_id):
    query = select(Task).where(Task.id == task_id)
    result = db.session.execute(query)
    task = result.scalars().first()

    input("Are you sure you want to delete this task? (y/n): ")
    if input == "y":
        db.session.delete(task)
        db.session.commit()
        print("Task deleted.")
        return task
    else:
        print("Task deletion cancelled.")
        return None
    
    
