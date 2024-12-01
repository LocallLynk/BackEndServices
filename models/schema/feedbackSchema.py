from . import ma
from marshmallow import fields

class FeedbackSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    comment = fields.String(required=False)
    rating = fields.Integer(required=True)
    created_on = fields.Date(required=False)
    reviewed_neighbor_id = fields.Integer(required=True)
    reviewer_id = fields.Integer(required=True)
    task_id = fields.Integer(required=True)
    reviewer = fields.Nested('NeighborSchema', only=['id', 'profile_pic', 'first_name', 'last_name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    reviewed_neighbor = fields.Nested('NeighborSchema', only=['id', 'profile_pic', 'first_name', 'last_name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    task = fields.Nested('TaskSchema', only=['id', 'description', 'created_on', 'status', 'task_paid', 'traded_task', 'task_neighbor_id', 'client_neighbor_id', 'skill_id'])

    class Meta:
        fields = ('id', 'comment', 'rating', 'created_on', 'reviewer_id', 'reviewed_neighbor_id', 'task_id', 'reviewer', 'reviewed_neighbor', 'task') #fields coming into feedback schema

feedback_schema = FeedbackSchema() #instantiating our feedback schema, returns a single feedback
feedbacks_schema = FeedbackSchema(many=True) # returns a list of feedbacks
