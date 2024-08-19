"""
posts/forms.py

This module defines the forms used in the application, including their fields
and validation logic.
"""
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    """
    Forms for creating and updating Post objects.

    Fields:
    - title: CharField for the post title.
    - content: TextField for the post content.

    Meta class:
    - Defines the model to use (Post) and the fields to include in the form.

    :param forms.ModelForm: Django's ModelForm class.
    """
    class Meta:
        """ g"""
        model = Post
        fields = ['title', 'content', 'author']


class SignupForm(UserCreationForm):
    """
    Forms for creating and updating User objects.

    Fields:
    - username
    - email
    - password1
    - password2
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    """
    Forms for authorising and authorising a user

    Fields:
    - username
    - password
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
