from database import db, Base
from models import Neighbor, Skill, Task, Feedback
from datetime import date
from sqlalchemy import select

def create_task(task_data):
    
    new_task = Task(
        task_neighbor_id=task_data['task_neighbor_id'],
        client_neighbor_id=task_data['client_neighbor_id'],
        description=task_data['description'],
        skill_id=task_data['skill_id'],
        status="open",
        task_paid=task_data['task_paid'],
        traded_task=task_data['traded_task'],
        created_on=date.today()
    )
    
    db.session.add(new_task)
    db.session.commit()
    db.session.refresh(new_task)
    
    return new_task

def get_all_tasks():
    
    query = select(Task)
    result = db.session.execute(query)
    return result.scalars().all()

def find_task_by_id(task_id):
    
    task = db.session.get(Task, task_id)
    if not task:
        raise ValueError("Task not found.")
    return task

def find_tasks_by_task_neighbor_id(task_neighbor_id):
    
    query = select(Task).where(Task.task_neighbor_id == task_neighbor_id)
    result = db.session.execute(query)
    if not result:
        raise ValueError("Tasks not found.")
    return result.scalars().all()

def find_tasks_by_client_neighbor_id(client_neighbor_id):
    
    query = select(Task).where(Task.client_neighbor_id == client_neighbor_id)
    result = db.session.execute(query)
    if not result:
        raise ValueError("Tasks not found.")
    return result.scalars().all()

def update_task(task_id, task_data):
    
    task = find_task_by_id(task_id)
    task.description = task_data.get('description', task.description)
    task.skill_id = task_data.get('skill_id', task.skill_id)
    task.status = task_data.get('status', task.status)
    task.task_paid = task_data.get('task_paid', task.task_paid)
    task.traded_task = task_data.get('traded_task', task.traded_task)
    if task.status not in ["open", "in_progress", "completed"]:
        raise ValueError("Invalid status. Please enter 'open', 'in_progress', or 'completed'.")
    db.session.commit()
    return task

def delete_task(task_id):
    
    task = find_task_by_id(task_id)
    db.session.delete(task)
    db.session.commit()
    print("Task deleted.")
    return task


# Placeholder for additional features:
# - Cart system: Tasks marked as traded could be added to a "cart" along with traded items.
# - Payment system: Manage task payment methods and status.
# - Task completion: When a task is marked as completed, it could trigger the feedback system.



