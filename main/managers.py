from django.contrib.auth.models import User
from django.db import models

class UserDataManager(models.Manager):
    def create_user(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        return self.create(user=user)