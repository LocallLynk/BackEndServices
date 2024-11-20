from . import ma
from marshmallow import fields

class CommentSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    content = fields.String(required=True)
    created_on = fields.Date(required=False)
    post_id = fields.Integer(required=True)
    neighbor_id = fields.Integer(required=False)
    neighbor = fields.Nested('NeighborSchema', only=['id', 'first_name', 'last_name', 'email', 'phone', 'username', 'zipcode', 'admin'])
    post = fields.Nested('PostSchema', only=['id', 'likes_count', 'dislikes_count', 'shares_count', 'comments_count', 'content', 'created_on', 'neighbor_id', 'neighbor', 'comments', 'likes', 'dislikes', 'shares'])

    class Meta:
        fields = ('id', 'content', 'created_on', 'post_id', 'neighbor_id', 'neighbor', 'post') #fields coming into comment schema

comment_schema = CommentSchema() #instantiating our comment schema
comments_schema = CommentSchema(many=True) # returns a list of comments