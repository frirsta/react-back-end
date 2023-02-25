from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from django.contrib.auth.models import User


class CreatePostTest(APITestCase):
    def setUp(self):
        john = User.objects.create_user(username='john', password='1234')

    def test_create_post(self):
        """
        Ensures we can create a post object.
        """
        john = User.objects.get(username='john')
        Post.objects.create(owner=john, caption='caption')
        response = self.client.get('/posts/')
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().caption, 'caption')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
