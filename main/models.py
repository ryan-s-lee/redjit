from django.db import models

# Create your models here.

class Communities:
    name = models.CharField()

class Author:
    username = models.CharField()
    userhandle = models.CharField(primary_key=True)
    birthday = models.DateField()
    communities = models.ManyToManyField(Communities)

class Post:
    title = models.CharField()
    content = models.TextField()
    creation_time = models.DateTimeField()
    last_edit_time = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)