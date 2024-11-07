from . import ma
from marshmallow import fields

class FeedbackSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    comment = fields.String(required=False)
    rating = fields.Integer(required=True)
    created_on = fields.Date(required=True)
    reviewer_id = fields.Integer(required=True)
    task_id = fields.Integer(required=True)
    reviewer = fields.Nested('NeighborSchema', only=['id', 'name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    reviewed_neighbor = fields.Nested('NeighborSchema', only=['id', 'name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    task = fields.Nested('TaskSchema', only=['id', 'title', 'description', 'neighbor_id', 'skill_id', 'status', 'created_on', 'due_date', 'neighbor'])

    class Meta:
        fields = ('id', 'comment', 'rating', 'created_on', 'reviewer_id', 'task_id', 'reviewer', 'reviewed_neighbor', 'task') #fields coming into feedback schema

feedback_schema = FeedbackSchema() #instantiating our feedback schema, returns a single feedback
feedbacks_schema = FeedbackSchema(many=True) # returns a list of feedbacks
