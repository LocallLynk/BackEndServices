from database import db
from models import Neighbor, Skill, Task, Feedback
from datetime import date
from sqlalchemy import select

def create_task(task_data):
    """Creates a new task and saves it to the database."""
    new_task = Task(
        task_neighbor_id=task_data['task_neighbor_id'],
        client_neighbor_id=task_data['client_neighbor_id'],
        title=task_data['title'],
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

def find_task_by_id(task_id):
    """Finds a task by its ID."""
    task = db.session.get(Task, task_id)
    if not task:
        raise ValueError("Task not found.")
    return task

def find_tasks_by_task_neighbor_id(task_neighbor_id):
    """Finds tasks by the task neighbor ID."""
    query = select(Task).where(Task.task_neighbor_id == task_neighbor_id)
    result = db.session.execute(query)
    return result.scalars().all()

def find_tasks_by_client_neighbor_id(client_neighbor_id):
    """Finds tasks by the client neighbor ID."""
    query = select(Task).where(Task.client_neighbor_id == client_neighbor_id)
    result = db.session.execute(query)
    return result.scalars().all()

def update_task_status(task_id, new_status):
    """Updates the status of a task."""
    task = find_task_by_id(task_id)
    task.status = new_status
    db.session.commit()
    return task

def update_task_payment_status(task_id, task_paid):
    """Updates the payment status of a task."""
    task = find_task_by_id(task_id)
    task.task_paid = task_paid
    db.session.commit()
    return task

def update_traded_task(task_id, traded_task):
    """Updates the traded task attribute of a task."""
    task = find_task_by_id(task_id)
    task.traded_task = traded_task
    db.session.commit()
    return task

def update_task(task_id, task_data):
    """Updates various fields of a task."""
    task = find_task_by_id(task_id)
    task.title = task_data.get('title', task.title)
    task.description = task_data.get('description', task.description)
    task.skill_id = task_data.get('skill_id', task.skill_id)
    db.session.commit()
    return task

def delete_task(task_id, confirm_deletion):
    """Deletes a task if confirmed."""
    task = find_task_by_id(task_id)
    if confirm_deletion.lower() == 'y':
        db.session.delete(task)
        db.session.commit()
        print("Task deleted.")
        return task
    else:
        print("Task deletion cancelled.")
        return None

# Placeholder for additional features:
# - Cart system: Tasks marked as traded could be added to a "cart" along with traded items.
# - Payment system: Manage task payment methods and status.
# - Task completion: When a task is marked as completed, it could trigger the feedback system.



