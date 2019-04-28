from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

def index(request):
    todo_list = Post.objects.order_by('deadline')
    return render(request, 'todo/index.html', {'todo_list': todo_list})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'todo/detail.html', context)

def add(request):
    form = PostForm(request.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('index'))

def delete(request, id=None):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))