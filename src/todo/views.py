from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from webpush import send_user_notification
from .models import Post
from .forms import PostForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

@login_required
def index(request):
    user = request.user
    todo_list = Post.objects.filter(author=user).order_by('deadline')
    # webpush
    # あとでVueに移植
    payload = {"head": "Welcome!", "body": "Hello World"}
    send_user_notification(user=user, payload=payload, ttl=1000)
    return render(request, 'index.html', {'todo_list': todo_list})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form})

def delete(request, id=None):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('index')

def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form, 'post': post})