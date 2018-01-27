from rest_framework import serializers

from apps.products.models import Category, Book
from apps.products.relations import AuthorRelatedField
from apps.profiles.models import Author


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


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    author = AuthorRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True, source='author')

    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                       write_only=True, source='categories', many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'slug',
            'isbn',
            'date_published',
            'price',
            'categories',
            'categories_id',
            'pages',
            'author',
            'author_id',
        )
