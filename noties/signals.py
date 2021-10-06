from django.db.models.signals import post_save

from noties.models import Notification, Like


def create_noti(sender, created, instance, **kwargs):
    if created:
        Notification.objects.create(
            post=instance.post,
            to=instance.post.user,
            come_from=instance.user,
        )


post_save.connect(create_noti, sender=Like)
