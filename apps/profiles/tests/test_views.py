from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from django.test import TestCase


from apps.profiles.models import Author
from apps.profiles.serializers import AuthorSerializer
from django.contrib.auth.models import User


class GetAllAuthorsTest(TestCase):
    """ Test module for GET all authors API """

    def setUp(self):
        self.factory = APIRequestFactory()

        user_data = {'username': 'test'}
        user = User.objects.create(
            is_active=False, **user_data)

        Author.objects.create(user=user)

    def test_get_all_authors(self):
        """
        Ensure we get all users created        
        """

        url = reverse('author-list')
        authors = Author.objects.all()
        serializer_context = {
            'request': self.factory.get(
                url,
                format='json'
            ),
        }
        serializer = AuthorSerializer(authors, many=True, context=serializer_context)

        response = self.client.get(url)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateAuthorTest(APITestCase):
    """ Test module for inserting a new author """

    def setUp(self):
        self.valid_author = {
            'user': {
                'username': 't1'
            }
        }

    def test_create_valid_author(self):
        """
        Ensure we can create a new profile object.
        """

        url = reverse('author-list')
        response = self.client.post(
            url,
            self.valid_author,
            format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().user.username, 't1')
        self.assertEqual(Author.objects.get().user.is_active, False)

    def test_fails_to_create_if_author_username_field_is_missing(self):
        """
        Ensure we can't create an author without a username
        """

        invalid_data = {'user': {}}

        url = reverse('author-list')
        response = self.client.post(
            url,
            invalid_data,
            format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('user' in response.data)
        self.assertTrue('username' in response.data['user'])


class UpdateSingleAuthorTest(APITestCase):
    """ Test module for updating an existing author record """

    def setUp(self):
        user_data = {'username': 'author.test.case'}
        user = User.objects.create(
            is_active=False,
            **user_data
        )

        self.author_test_case = Author.objects.create(user=user)
        self.valid_payload = {
            'bio': 'lorem ipsum dolor',
            'user': {}
        }

    def test_update_valid_author(self):
        """
        Ensure can update the attributes of an author
        """

        url = reverse(
            'author-detail',
            kwargs={'pk': self.author_test_case.pk}
        )
        response = self.client.put(
            url,
            data=self.valid_payload,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], self.valid_payload['bio'])

    def test_update_valid_author_user_fk(self):
        """
        Ensure can update the user fk of an author
        """

        author_data = {
            'user': {
                'username': 'test.case',
                'first_name': 'test',
                'last_name': 'case'
            }
        }

        url = reverse(
            'author-detail',
            kwargs={'pk': self.author_test_case.pk}
        )
        response = self.client.put(
            url,
            data=author_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], author_data['user']['username'])
        self.assertEqual(response.data['user']['first_name'], author_data['user']['first_name'])
        self.assertEqual(response.data['user']['last_name'], author_data['user']['last_name'])

    def test_fails_to_update_if_author_username_field_is_duplicate(self):
        """
        Ensure we can't update an author with duplicate username
        """

        invalid_author_data = {
            'user': {
                'username': 'author.test.case'
            }
        }

        url = reverse(
            'author-detail',
            kwargs={'pk': self.author_test_case.pk}
        )
        response = self.client.put(
            url,
            data=invalid_author_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleAuthorTest(APITestCase):
    """ Test module for deleting an existing author record """

    def setUp(self):
        user_data = {'username': 'john.bravo'}
        user = User.objects.create(
            is_active=False, **user_data)

        self.john_bravo = Author.objects.create(user=user)

    def test_delete_valid_author(self):
        """
        Ensure we can delete an existing author
        """

        url = reverse(
            'author-detail',
            kwargs={'pk': self.john_bravo.pk}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_fails_to_delete_for_invalid_author_pk_field(self):
        """
        Ensure we can't delete an author who does not exist
        """

        invalid_pk = 120

        url = reverse(
            'author-detail',
            kwargs={'pk': invalid_pk}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
