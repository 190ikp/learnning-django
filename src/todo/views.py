from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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
    return render(request,'todo/signup.html',{'form':form})

@login_required
def index(request):
    todo_list = Post.objects.order_by('deadline')
    return render(request, 'todo/index.html', {'todo_list': todo_list})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'todo/detail.html', {'post': post})

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'todo/add.html', {'form': form})

def delete(request, id=None):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('index')

def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', pk=post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'todo/edit.html', {'form': form})