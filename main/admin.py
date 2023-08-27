from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MainPost)
admin.site.register(models.CommentPost)
admin.site.register(models.UserData)
admin.site.register(models.Community)