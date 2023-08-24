from django.forms import ModelForm
from . import models
from django.contrib.auth.models import User
# There's a dependency between main and api!!! Is that something we can avoid?
import api.models as models

class RegistrationForm(ModelForm):
    pass

class CreatePostForm(ModelForm):
    pass

class EditPostForm(ModelForm):
    pass

class CreateCommunityForm(ModelForm):
    pass

class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]