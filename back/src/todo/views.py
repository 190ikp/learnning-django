from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# add following library for webpush
from django.conf import settings
# from django.http.response import JsonResponse, HttpResponse
# from django.views.decorators.http import require_GET, require_POST
# from django.views.decorators.csrf import csrf_exempt
# from webpush import send_user_notification
# import json
# import datetime


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
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    todo_list = Post.objects.filter(author=user).order_by('deadline')
    content = {
        'todo_list': todo_list,
        'vapid_key': vapid_key,
    }
    return render(request, 'index.html', content)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
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

def delete(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'edit.html', context)

# @required_POST
# def send_push(request):
#     user = request.user
#     todo = Post.objects.filter(author=user)

#     remind_text = get_object_or_404(Post.WHEN_REMIND, pk=pk)
#     message = '期限' + remind_text + 'です！'
#     payload = {
#         'head': '期限通知',
#         'body': message
#     }
#     send_user_notification(user=user, payload=payload, ttl=1000)