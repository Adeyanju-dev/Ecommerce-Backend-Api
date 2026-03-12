from django.db import models
from orders.models import Order


class Payment(models.Model):

    PAYMENT_METHODS = [
        ("card", "Card"),
        ("bank_transfer", "Bank Transfer"),
        ("paypal", "Paypal"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("successful", "Successful"),
        ("failed", "Failed"),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    payment_reference = models.CharField(max_length=100, unique=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHODS
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_reference