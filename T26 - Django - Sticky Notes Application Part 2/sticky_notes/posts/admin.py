"""
posts/admin.py

This module registers the application's models with the Django admin site and
customizes the admin interface.
"""
from django.contrib import admin
from .models import Post
from .models import Author
from .models import User


# Register your models here.

# Post model
admin.site.register(Post)

# Author model
admin.site.register(Author)

# User model
admin.site.register(User)
