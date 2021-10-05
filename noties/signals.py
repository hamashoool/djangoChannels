from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save

from noties.models import Notification, Like


def create_noti(sender, created, instance, **kwargs):
    if created:
        Notification.objects.create(
            post=instance.post,
            to=instance.post.user,
            come_from=instance.user,
        )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notification_broadcast",
            {
                'type': 'send_notification',
                'message': 'You got notification'
            }
        )


post_save.connect(create_noti, sender=Like)
