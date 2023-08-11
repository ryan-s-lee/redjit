from django.db import models

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=32)

class User(models.Model):
    username = models.CharField(max_length=32)
    birthday = models.DateField()
    communities = models.ManyToManyField(Community)

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    creation_time = models.DateTimeField()
    last_edit_time = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)