from rest_framework import viewsets, filters

from apps.products.models import Category, Book
from apps.products.serializers import CategorySerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('title', 'author__user__username')
    ordering_fields = '__all__'
    ordering = ('-date_published', 'title')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
