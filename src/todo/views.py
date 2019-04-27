from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def index(request):
    todo_list = Post.objects.all()
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todo/index.html', context)