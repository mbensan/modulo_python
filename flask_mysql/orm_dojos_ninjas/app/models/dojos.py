from tortoise.models import Model
from tortoise import fields



class Dojo(Model):
    name = fields.CharField(45)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)