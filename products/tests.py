from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Category, Product

User = get_user_model()


class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            category=self.category,
            name="iPhone 13",
            description="Smartphone",
            price=800,
            stock_quantity=10,
            is_active=True,
        )

    def test_anyone_can_view_products(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_normal_user_cannot_create_product(self):
        user = User.objects.create_user(
            email="user@example.com",
            username="user",
            password="StrongPass123"
        )

        login = self.client.post("/api/auth/login/", {
            "email": "user@example.com",
            "password": "StrongPass123"
        }, format="json")

        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        response = self.client.post("/api/products/", {
            "name": "Samsung S24",
            "description": "Phone",
            "price": 1000,
            "stock_quantity": 5,
            "category_id": self.category.id
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)