from rest_framework import viewsets

from apps.products.models import Category
from apps.products.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()