from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import Author


@receiver(post_delete, sender=Author)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:  # just in case user is not specified
        instance.user.delete()
