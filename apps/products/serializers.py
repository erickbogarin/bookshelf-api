from rest_framework import serializers

from apps.products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )
