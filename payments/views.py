import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from orders.models import Order
from .models import Payment
from .serializers import PaymentSerializer


class InitiatePaymentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, order_number):

        try:
            order = Order.objects.get(order_number=order_number, user=request.user)
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if order.payment_status == "paid":
            return Response(
                {"error": "Order already paid"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if hasattr(order, "payment"):
            return Response(
                {"error": "Payment already initiated for this order"},
                status=status.HTTP_400_BAD_REQUEST
            )

        payment = Payment.objects.create(
            order=order,
            payment_reference=str(uuid.uuid4()),
            amount=order.total_price,
            payment_method=request.data.get("payment_method", "card"),
        )

        serializer = PaymentSerializer(payment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class VerifyPaymentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, payment_reference):

        try:
            payment = Payment.objects.get(payment_reference=payment_reference)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        payment.status = "successful"
        payment.save()

        order = payment.order
        order.payment_status = "paid"
        order.save()

        return Response({"message": "Payment successful"})