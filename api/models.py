from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    date=models.DateField()

class Users(models.Model):
    username=models.CharField(max_length=32)
    description=models.TextField()
    creation_date = models.DateField()