from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from products.models import Category, Product
from cart.models import Cart, CartItem
from .models import Order

User = get_user_model()


class CheckoutTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="buyer@example.com",
            username="buyer",
            password="StrongPass123"
        )

        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            category=self.category,
            name="Laptop",
            description="Good laptop",
            price=500,
            stock_quantity=10,
            is_active=True,
        )

        login = self.client.post("/api/auth/login/", {
            "email": "buyer@example.com",
            "password": "StrongPass123"
        }, format="json")

        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_user_can_checkout(self):
        self.client.post("/api/cart/add/", {
            "product_id": self.product.id,
            "quantity": 2
        }, format="json")

        response = self.client.post("/api/orders/checkout/", {
            "full_name": "Mike John",
            "phone_number": "08012345678",
            "address": "12 Allen Avenue",
            "city": "Ikeja",
            "state": "Lagos",
            "country": "Nigeria"
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_checkout_reduces_stock(self):
        self.client.post("/api/cart/add/", {
            "product_id": self.product.id,
            "quantity": 2
        }, format="json")

        self.client.post("/api/orders/checkout/", {
            "full_name": "Mike John",
            "phone_number": "08012345678",
            "address": "12 Allen Avenue",
            "city": "Ikeja",
            "state": "Lagos",
            "country": "Nigeria"
        }, format="json")

        self.product.refresh_from_db()
        self.assertEqual(self.product.stock_quantity, 8)