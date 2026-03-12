from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            "id",
            "payment_reference",
            "amount",
            "payment_method",
            "status",
            "created_at",
        ]