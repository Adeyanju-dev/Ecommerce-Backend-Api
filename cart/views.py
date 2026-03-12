from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartItem
from .serializers import CartSerializer
from products.models import Product


class CartView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class AddToCartView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        product = Product.objects.get(id=product_id)

        if not product.is_active:
            return Response(
                {"error": "This product is not available"},
                status=400
            )
        
        if int(quantity) < 1:
            return Response(
                {"error": "Quantity must be atleast 1"},
                status=400
            )

        cart, created = Cart.objects.get_or_create(user=request.user)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantity += int(quantity)
        else:
            item.quantity = int(quantity)

        item.save()

        return Response({"message": "Item added to cart"}) 

class RemoveFromCartView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):

        item = CartItem.objects.get(id=item_id, cart__user=request.user)
        item.delete()

        return Response({"message": "Item removed"})   