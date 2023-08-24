from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from django.core import validators

class Community(models.Model):
    name = models.CharField(max_length=32, unique=True, validators=[validators.validate_slug])
    def __str__(self):
        return self.name
    

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=32, unique=True)
    birthday = models.DateField()
    communities = models.ManyToManyField(Community)
    def __str__(self) -> str:
        return self.username

class Post(models.Model):
    class Meta:
        abstract = True
        ordering=["creation_time"]

    def creation_time_default():
        return datetime.now()

    def last_edit_time_default():
        return datetime.now()

    content = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now)
    last_edit_time = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(UserData, null=True, on_delete=models.SET_NULL)
    community = models.ForeignKey(Community, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title + "#" + str(self.pk)

class MainPost(Post):
    title = models.CharField(max_length=256)

class CommentPost(Post):
    parent = models.OneToOneField(Post, on_delete=models.CASCADE)