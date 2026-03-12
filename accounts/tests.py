from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTests(APITestCase):
    def test_user_can_register(self):
        data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "StrongPass123",
            "password_confirm": "StrongPass123",
        }

        response = self.client.post("/api/auth/register/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, "testuser@example.com")

    def test_user_can_login(self):
        User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="StrongPass123"
        )

        data = {
            "email": "testuser@example.com",
            "password": "StrongPass123"
        }

        response = self.client.post("/api/auth/login/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)