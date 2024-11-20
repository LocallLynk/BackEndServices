from . import ma
from marshmallow import fields

class NeighborSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    zipcode = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    overall_rating = fields.Float(required=False)
    num_ratings = fields.Integer(required=False)
    num_rated = fields.Integer(required=False)
    created_on = fields.Date(required=False)
    task_neighbor = fields.Boolean(required=False)
    client_neighbor = fields.Boolean(required=False)
    admin = fields.Boolean(required=False)
    skills = fields.List(fields.Nested('SkillSchema'), required=False)
    
        
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'username', 'password', 'zipcode', 'admin', 'num_ratings', 'skills', 'overall_rating') #fields coming into neighbor schema
            
neighbor_schema = NeighborSchema() #instantiating our neighbor schema
neighbors_schema = NeighborSchema(many=True, exclude=["password"]) # returns a list of neighbors, excludes the password field
neighbor_login = NeighborSchema(exclude=["first_name", "last_name", "phone", "username","zipcode","id"]) #returns a neighbor object with only the email and password fields
neighborz_schema = NeighborSchema(exclude=["password"]) #returns neighbor info without the PW field