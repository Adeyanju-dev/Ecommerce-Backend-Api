import uuid
from decimal import Decimal

from cart.models import Cart
from .models import Order, OrderItem, ShippingAddress


def create_order_from_cart(user, shipping_data):

    cart = Cart.objects.get(user=user)

    cart_items = cart.items.all()

    if not cart_items.exists():
        raise ValueError("Cart is empty")

    order = Order.objects.create(
        user=user,
        order_number=str(uuid.uuid4()).split("-")[0].upper()
    )

    total_price = Decimal("0.00")

    for item in cart_items:

        product = item.product

        if item.quantity > product.stock_quantity:
            raise ValueError(f"Not enough stock for {product.name}")

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item.quantity,
            price=product.price
        )

        product.stock_quantity -= item.quantity
        product.save()

        total_price += product.price * item.quantity

    order.total_price = total_price
    order.save()

    ShippingAddress.objects.create(
        order=order,
        full_name=shipping_data.get("full_name"),
        phone_number=shipping_data.get("phone_number"),
        address=shipping_data.get("address"),
        city=shipping_data.get("city"),
        state=shipping_data.get("state"),
        country=shipping_data.get("country"),
    )

    cart_items.delete()

    return order