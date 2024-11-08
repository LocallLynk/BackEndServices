from . import ma
from marshmallow import fields

class NeighborSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    zipcode = fields.String(required=True)
    admin = fields.Integer(required=False)
    
        
    class Meta:
        fields = ('id', 'name', 'email', 'phone', 'username', 'password', 'zipcode', 'admin') #fields coming into neighbor schema
            
neighbor_schema = NeighborSchema() #instantiating our neighbor schema
neighbors_schema = NeighborSchema(many=True, exclude=["password"]) # returns a list of neighbors, excludes the password field
neighbor_login = NeighborSchema(exclude=["name", "phone", "username","id"]) #returns a neighbor object with only the username and password fields