from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name',
                  'last_name', 'email', 'groups', 'is_active']
