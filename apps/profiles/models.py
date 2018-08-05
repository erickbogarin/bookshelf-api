from django.db import models
from django.contrib.auth.models import User

class AuthorUsernameManager(models.Manager):
    def has_username(self, data, pk=None):
        try:
            username = data['user']['username']
            queryset = User.objects.filter(username__iexact=username)
            if (pk):
                queryset = queryset.exclude(pk=pk)
            return queryset.exists()
        except:
            return False

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    image = models.URLField(blank=True)
    objects = AuthorUsernameManager()
