from . import ma
from marshmallow import fields

class TaskSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    description = fields.String(required=True)
    created_on = fields.Date(required=True)
    status = fields.String(required=True)
    task_paid = fields.Boolean(required=True)
    traded_task = fields.Boolean(required=True)
    task_neighbor_id = fields.Integer(required=True)
    client_neighbor_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'description', 'created_on', 'status', 'task_paid', 'traded_task', 'task_neighbor_id', 'client_neighbor_id', 'skill_id')

task_schema = TaskSchema() #instantiating our task schema
tasks_schema = TaskSchema(many=True) # returns a list of tasks