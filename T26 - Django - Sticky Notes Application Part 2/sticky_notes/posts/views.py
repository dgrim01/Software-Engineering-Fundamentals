"""
posts/views.py

View functions and class-based views for the sticky_notes application,
managing HTTP requests and rendering responses.
"""
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm, LoginForm


# Create your views here.

# Views for Post
def post_list(request):
    """
    View to display a list of all posts.

    :param request: HTTP request object.
    :return: Rendered template with a list of posts.
    """
    posts = Post.objects.all()

    # Creating a context dictionary to pass data
    context = {
        'posts': posts,
        'page_title': 'List of Posts',
    }

    return render(request, 'posts/post_list.html', context)


def post_list_loggedin(request):
    """
    View to display a list of all posts and displays access to functionality
    when logged in.

    :param request: HTTP request object.
    :return: Rendered template with a list of posts.
    """
    posts = Post.objects.all()

    # Creating a context dictionary to pass data
    context = {
        'posts': posts,
        'page_title': 'List of Posts',
    }

    return render(request, 'posts/post_list_loggedin.html', context)


def post_detail(request, pk):
    """
    View to display details of specific post.

    :param request: HTTP request object.
    :param pk: Primary key of the post.
    :return: Rendered template with details of the specified posts.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    """
    View to create a new post

    :param request HTTP object.
    :return Rendered template for creating a new post.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = get_object_or_404(Author, name=request.user)
            else:
                post.author = None
            post.save()
            return redirect('post_list_loggedin')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


def post_update(request, pk):
    """
    View to update an existing post.

    :param request HTTP object.
    :param pk: Primary key of the post to be updated.
    :return: Rendered template for updating specified post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list_loggedin')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


def post_delete(request, pk):
    """
    View to delete an existing post.

    :param request HTTP object.
    :param pk: Primary key of the post to be updated.
    :return: Redirect to the post list after deletion.
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list_loggedin')


# Views for User
def signup_view(request):
    """
    If the user does not currently have an account on the system,
    this method allows them to register an account
    to be able to use the system.

    :param request HTTP object.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'posts/signup.html', {'form': form})


def login_view(request):
    """
    This method allows the user to input there username and password
    provided that they are already registered.

    :param request HTTP object.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('post_list_loggedin')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = LoginForm()
    return render(request, 'posts/login.html', {'form': form})


def logout_view(request):
    """
    This is a method to allow the user to logged out the system.

    :param request HTTP object.
    """
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('post_list')
