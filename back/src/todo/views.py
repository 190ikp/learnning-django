from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# add following library for webpush
# from django.http.response import JsonResponse, HttpResponse
# from django.views.decorators.http import require_GET, require_POST
# from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
# import json


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
    return render(request, 'index.html', {'todo_list': todo_list})

@login_required
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

@login_required
def delete(request, id=None):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('index')

@login_required
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
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'edit.html', context)

# @login_required
# def send_push(request):
#     user = request.user
#     remind_time = get_object_or_404(Post.when_remind)
#     remind_text = get_object_or_404(Post.WHEN_REMIND, pk=post_id)
#     message = '期限' + remind_text + 'です！'
#     payload = {
#         'head': '期限が近づいています！',
#         'body': message
#     }
#     send_user_notification(user=user, payload=payload, ttl=1000)

#     return

# def send_push(request):
#     try:
#         body = request.body
#         data = json.loads(body)

#         if 'head' not in data or 'body' not in data:
#             return JsonResponse(status=400, data={"message": "Invalid data format"})

#         user = request.user
#         payload = {'head': data['head'], 'body': data['body']}
#         send_user_notification(user=user, payload=payload, ttl=1000)

#         return JsonResponse(status=200, data={"message": "Web push successful"})
#     except TypeError:
#         return JsonResponse(status=500, data={"message": "An error occurred"})

# @require_GET
# def home(request):
#     webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
#     vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
#     user = request.user
#     return render(request, )