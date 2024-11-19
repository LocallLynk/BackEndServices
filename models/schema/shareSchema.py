from . import ma
from marshmallow import fields

class ShareSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    post_id = fields.Integer(required=True)
    post = fields.String(required=True)
    shared_on = fields.Date(required=False)
    neighbor_id = fields.Integer(required=True)
    neighbor = fields.Nested('NeighborSchema', only=['id', 'name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    
    class Meta:
        fields = ('id', 'post_id', 'post', 'shared_on', 'neighbor_id', 'neighbor') #fields coming into share schema

share_schema = ShareSchema() #instantiating our share schema
shares_schema = ShareSchema(many=True) # returns a list of shares