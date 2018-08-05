from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

from rest_framework import serializers

from apps.profiles.models import Author


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = User
        fields = ['id','url', 'username', 'first_name',
                  'last_name', 'email', 'groups', 'is_active']
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

class AuthorSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Author objects."""

    user = UserSerializer()

    class Meta:
        model = Author
        fields = ['id', 'bio', 'image', 'user']

    def create(self, validated_data):
        """Creates a new author"""

        user_data = validated_data.pop('user')

        user = User.objects.create(
            is_active=False,
            **user_data)

        author = Author.objects.create(user=user, **validated_data)

        return author

    def update(self, instance, validated_data):
        """Performs an update on an Author."""

        user_data = validated_data.pop('user')

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        for (key, value) in user_data.items():
            setattr(instance.user, key, value)

        instance.user.save()

        return instance
