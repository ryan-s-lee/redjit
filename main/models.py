from django.db import models

from datetime import datetime
from django.contrib.auth.models import User, Group
from django.core import validators
from . import managers


class Community(models.Model):
    name = models.CharField(
        max_length=32, unique=True, validators=[validators.validate_slug]
    )
    rules = models.TextField(blank=True)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class UserData(models.Model):
    objects = managers.UserDataManager()

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdata")
    birthday = models.DateField(default=datetime.now)
    communities = models.ManyToManyField(Community, blank=True, related_name="user_set")
    moderating = models.ManyToManyField(
        Community, blank=True, related_name="moderator_set"
    )

    def __str__(self) -> str:
        return f"{self.user.username}"


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(UserData, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, related_name="replies")
    creation_time = models.DateTimeField(default=datetime.now)
    last_edit_time = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.title + "#" + str(self.pk)



class Thread(models.Model):
    title = models.CharField(max_length=256)
    root_post = models.OneToOneField(
        Post, on_delete=models.PROTECT
    )
    community = models.ForeignKey(Community, blank=False, on_delete=models.CASCADE)
    class Meta:
        ordering = ["-root_post__creation_time"]
