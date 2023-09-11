from django.contrib.auth.models import User
from django.db import models

class UserDataManager(models.Manager):
    def create_user(self, username, password):
        user = User.objects.create_user(username, None, password)
        return self.create(user=user)