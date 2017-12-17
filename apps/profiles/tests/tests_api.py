from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.profiles.models import Author


class AuthorTests(APITestCase):
    def test_create_author(self):
        """
        Ensure we can create a new profile object.
        """
        url = reverse('author-list')
        data = { 'user': {'username': 't1'}}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().user.username, 't1')
        self.assertEqual(Author.objects.get().user.is_active, False)