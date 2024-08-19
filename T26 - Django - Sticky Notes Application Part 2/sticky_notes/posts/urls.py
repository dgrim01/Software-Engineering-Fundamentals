"""
posts/urls.py

This module contains the URL routing configuration for the application.
"""
from django.urls import path
from .views import post_list, post_detail, post_create, post_update, \
    post_delete, post_list_loggedin
from .views import signup_view, login_view, logout_view


urlpatterns = [
    # URL Patterns for Post
    # URL pattern for displaying a list of all posts
    path('', post_list, name='post_list'),

    # URL pattern for displaying details details of specific post
    path('posts/<int:pk>/', post_detail, name='post_detail'),

    # URL pattern for creating a new post
    path('posts/new/', post_create, name='post_create'),

    # URL pattern for updating an existing post
    path('posts/<int:pk>/edit/', post_update, name='post_update'),

    # URL pattern for deleting an existing post
    path('posts/<int:pk>/delete/', post_delete, name='post_delete'),

    # URL pattern for when the user has logged in and been authorised
    path('posts/loggedinlist', post_list_loggedin, name='post_list_loggedin'),

    # URL Patterns for User
    # URL pattern for signup user
    path('posts/signup/', signup_view, name='signup'),
    # URL pattern for login
    path('posts/login/', login_view, name='login'),
    # URL pattern for logout
    path('posts/logout/', logout_view, name='logout'),
]
