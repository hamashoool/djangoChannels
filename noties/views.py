from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
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

    return render(request, 'noties/home.html', context)


def like(request, post_id):
    post = Post.objects.get(id=post_id)
    Like.objects.create(
        user=request.user,
        post=post,
    )

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_to_"+str(post.user.id),
        {
            'type': 'send_notification',
            'message': 'You got notification',
            'post_id': post.id,
        }
    )
    return render(request, 'noties/likes.html', {'post': post})
