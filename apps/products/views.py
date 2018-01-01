from rest_framework import viewsets

from apps.products.models import Category, Book
from apps.products.serializers import CategorySerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()