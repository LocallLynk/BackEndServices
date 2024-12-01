from . import ma
from marshmallow import fields

class ShareSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    post_id = fields.Integer(required=True)
    shared_on = fields.Date(required=False)
    neighbor_id = fields.Integer(required=False)
    content = fields.String(required=True)

    neighbor = fields.Nested('NeighborSchema', only=['id', 'profile_pic', 'first_name', 'last_name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    post = fields.Nested('PostSchema', only=['id', 'title', 'likes_count', 'dislikes_count', 'shares_count', 'comments_count', 'content', 'created_on', 'neighbor_id', 'neighbor', 'comments', 'likes', 'dislikes', 'shares'])
    
    class Meta:
        fields = ('id', 'post_id', 'post', 'content', 'shared_on', 'neighbor_id', 'neighbor') #fields coming into share schema

share_schema = ShareSchema() #instantiating our share schema
shares_schema = ShareSchema(many=True) # returns a list of shares