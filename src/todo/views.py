from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

def index(request):
    todo_list = Post.objects.all()
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todo/index.html', context)

def add(request):
    form = PostForm(request.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('index'))

def delete(req, id=None):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))