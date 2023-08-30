from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import authenticate


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ["username", "email"]


class CreatePostForm(forms.ModelForm):
    pass


class EditPostForm(forms.ModelForm):
    pass


class CreateCommunityForm(forms.ModelForm):
    class Meta:
        model = models.Community
        fields = ["name", "description", "rules"]


class SignInForm(forms.Form):
    username_validator = UnicodeUsernameValidator()
    username = forms.CharField(max_length=150, validators=[username_validator])
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        # determine if a user actually exists.
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("No user with this username and password exist.")
