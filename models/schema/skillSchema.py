from . import ma
from marshmallow import fields

class SkillSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    name = fields.String(required=True)
    category = fields.String(required=True)
    experience = fields.String(required=True)
    description = fields.String(required=True)
    
    
    class Meta:
        fields = ('id', 'name', 'category', 'experience','description','neighbor_id') #fields coming into skill schema

skill_schema = SkillSchema() #instantiating our skill schema
skills_schema = SkillSchema(many=True) # returns a list of skills