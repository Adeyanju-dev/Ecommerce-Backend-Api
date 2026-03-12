from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from products.models import Product
from .models import Review
from .serializers import ReviewSerializer


class ProductReviewListCreateView(APIView):

    def get(self, request, product_slug):

        product = Product.objects.get(slug=product_slug)

        reviews = product.reviews.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)

    def post(self, request, product_slug):

        product = Product.objects.get(slug=product_slug)

        if Review.objects.filter(user=request.user, product=product).exists():
            return Response(
                {"error": "You already reviewed this product"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)