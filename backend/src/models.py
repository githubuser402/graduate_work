from tortoise import Tortoise, models, fields
from typing import List

class User(models.Model):
    id : int = fields.IntField(pk=True)
    username : str = fields.CharField(max_length=50)
    password : str = fields.CharField(max_length=50)


class Picture:
    id : int = fields.IntField(pk=True)
    link : str = fields.CharField(max_length=50)


class Video:
    id : int = fields.IntField(pk=True)
    link : str = fields.CharField(max_length=70)


class Dish(models.Model):
    id : int = fields.IntField(pk=True)
    title : str = fields.CharField(max_length=200)
    description : str = fields.TextField()
    images : List =  fields.ManyToManyField("models.Picture")
    videos : List = fields.ManyToManyField("models.Videos")
    users : List = fields.ManyToManyField("models.User")


