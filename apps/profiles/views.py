from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from apps.profiles.models import Author
from apps.profiles.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def update(self, request, pk=None):
        serializer_context = {'request': request}

        try:
            serializer_instance = Author.objects.get(pk=pk)
        except Author.DoestNotExist:
            raise NotFound('Author not found')

        serializer_data = request.data

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
