from django.contrib.auth.models import User
from rest_framework import serializers

from apps.profiles.models import Author
from apps.user.serializers import UserSerializer

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author
        fields = ['bio', 'image', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(
            is_active=False, **user_data)
        author = Author.objects.create(user=user, **validated_data)
        return author
