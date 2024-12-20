from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

from django.urls import reverse

from django.contrib.auth.models import User

class BookTests(APITestCase):
    def setUp(self):
        """
        Set up the test by creating a test instance of Book and a user for session authentication.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.obj = Book.objects.create(title='Test Object books')
        self.url = reverse('books-list')

    def test_get_books(self):
        """
        Test the GET method for the Book API endpoint.
        """
        self.client.login(username='testuser', password='testpassword')
        self.client.defaults['HTTP_X_CSRFTOKEN'] = 'foo'
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure one object is returned
        self.assertEqual(response.data[0]['title'], 'Test Object books')  # Ensure correct object data
