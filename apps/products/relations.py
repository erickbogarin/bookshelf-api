from rest_framework import serializers

from apps.profiles.models import Author


class AuthorRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Author.objects.all()

    def to_internal_value(self, data):
        author, created = Author.objects.get_or_create(author=data, slug=data.lower())

        return author

    def to_representation(self, value):
        return {
            'username': value.user.username,
            'email': value.user.email,
            'first_name': value.user.first_name,
            'last_name': value.user.last_name,
            'bio': value.bio,
        }
