from django.http import HttpResponse
from django.shortcuts import render

from .models import Post, Notification, Like


def home(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts

    noties = Notification.objects.filter(to=request.user)
    context['noties'] = noties
    context['noti_count'] = noties.count()

    context['room_name'] = 'broadcast'
    return render(request, 'noties/home.html', context)


def like(request, post_id):
    post = Post.objects.get(id=post_id)
    Like.objects.create(
        user=request.user,
        post=post,
    )
    return render(request, 'noties/likes.html', {'post': post})
