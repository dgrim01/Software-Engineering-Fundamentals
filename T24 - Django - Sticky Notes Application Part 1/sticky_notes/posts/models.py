"""
posts/models.py

Data models for the sticky_notes application, defining the database schema and
relationships.
"""
from django.db import models


# Create your models here.
class Post(models.Model):
    """
    Model representing a bulletin board post.

    Fields:
    - title: CharField representing the title of a post
    - content: TextField for the cotent of a post
    - created_at: DateTime representing the current date and time the post
        was created.
    Relationships:
    - author: Forgein representing the author of the post.
    Methods:
    - No specific methods are defined in this model

    :param models.Model: Django's base model class.

    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define a ForgeinKey for the author's relationship
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
                               null=True, blank=True)


class Author(models.Model):
    """
    Models representing the author of a bulletin board post

    Fields:
    - name: CharField for the author's name
    Methods:
    - No specific methods are not defined in this model.

    :param models.Model: Django's base model class.

    """
    name = models.CharField(max_length=255)


class User(models.Model):
    """
    Models representing the user of a bulletin board post

    Fields:
    - username: ChardField for user's username
    - email: EmailField for user's email
    - password1: CharField for user's password1
    - password2: CharField for user's password2

    Methods:
    - No specific methods are not defined in this model.

    """
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
