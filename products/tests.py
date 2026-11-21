from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ReviewPermissionTests(APITestCase):
    def test_anonymous_user_cannot_create_review(self):
        response = self.client.post(
            reverse('review-list'),
            {'product': 1, 'content': 'Test review', 'rating': 5},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
