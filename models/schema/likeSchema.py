from . import ma
from marshmallow import fields

class LikeSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    post_id = fields.Integer(required=True)
    neighbor_id = fields.Integer(required=False)
    liked_on = fields.Date(required=False)
    neighbor = fields.Nested('NeighborSchema', only=['id', 'profile_pic', 'first_name', 'last_name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    post = fields.Nested('PostSchema', only=['id', 'likes_count', 'dislikes_count', 'shares_count', 'comments_count', 'content', 'created_on', 'neighbor_id', 'neighbor', 'comments', 'likes', 'dislikes', 'shares'])
    
    class Meta:
        fields = ('id', 'post_id', 'neighbor_id', 'neighbor', 'liked_on', 'post') #fields coming into like schema

like_schema = LikeSchema() #instantiating our like schema
likes_schema = LikeSchema(many=True) # returns a list of likes