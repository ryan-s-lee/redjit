from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
admin.site.register(models.Thread)
admin.site.register(models.Post)
admin.site.register(models.Community)
admin.site.register(models.UserData)