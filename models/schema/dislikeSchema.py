from . import ma
from marshmallow import fields

class DislikeSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    post_id = fields.Integer(required=True)
    neighbor_id = fields.Integer(required=False)
    disliked_on = fields.Date(required=False)
    neighbor = fields.Nested('NeighborSchema', only=['id', 'first_name', 'last_name', 'email', 'phone', 'username', 'zipcode', 'admin']) 
    post = fields.Nested('PostSchema', only=['id', 'likes_count', 'dislikes_count', 'shares_count', 'comments_count', 'content', 'created_on', 'neighbor_id', 'neighbor', 'comments', 'likes', 'dislikes', 'shares'])
    
    class Meta:
        fields = ('id', 'post_id', 'neighbor_id', 'disliked_on', 'neighbor', 'post') #fields coming into dislike schema

dislike_schema = DislikeSchema() #instantiating our dislike schema
dislikes_schema = DislikeSchema(many=True) # returns a list of dislikes