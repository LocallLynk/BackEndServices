from . import ma
from marshmallow import fields

class PostSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    title = fields.String(required=True)
    likes_count = fields.Integer(required=False)
    dislikes_count = fields.Integer(required=False)
    shares_count = fields.Integer(required=False)
    comments_count = fields.Integer(required=False)
    content = fields.String(required=True)
    created_on = fields.Date(required=False)
    neighbor_id = fields.Integer(required=False)
    neighbor = fields.Nested('NeighborSchema', only=['id', 'profile_pic', 'first_name', 'last_name', 'username', 'zipcode'])
    comments = fields.Nested('CommentSchema', only=['id', 'content', 'created_on', 'neighbor_id', 'neighbor'], many=True)
    likes = fields.Nested('LikeSchema', only=['id', 'neighbor_id', 'neighbor'], many=True)
    dislikes = fields.Nested('DislikeSchema', only=['id', 'neighbor_id', 'neighbor'], many=True)
    shares = fields.Nested('ShareSchema', only=['id', 'shared_on', 'neighbor_id'], many=True)
    
    class Meta:
        fields = ('id', 'title', 'likes_count', 'dislikes_count', 'shares_count', 'comments_count', 'content', 'created_on', 'neighbor_id', 'neighbor', 'comments', 'likes', 'dislikes', 'shares') #fields coming into post schema

post_schema = PostSchema() 
posts_schema = PostSchema(many=True) # returns a list of posts