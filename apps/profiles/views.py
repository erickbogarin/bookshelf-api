from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status, filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from apps.profiles.models import Author
from apps.profiles.serializers import AuthorSerializer
from apps.profiles.exceptions import UsernameExists


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('user__first_name', 'user__last_name',)
    ordering_fields = ('user__first_name', 'user__last_name',)

    def create(self, request, pk=None):
        if Author.objects.has_username(request.data):
            raise UsernameExists()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):

        serializer_context = {'request': request}

        try:
            serializer_instance = Author.objects.get(pk=pk)
        except Author.DoestNotExist:
            raise NotFound('Author not found')

        serializer_data = request.data

        if Author.objects.has_username(serializer_data, serializer_instance.pk):
            raise UsernameExists()

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
