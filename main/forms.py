from django.forms import ModelForm
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