from django.urls import path
from .views import CheckoutView, UserOrderListView, OrderDetailView

urlpatterns = [
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("", UserOrderListView.as_view(), name="user-orders"),
    path("<str:order_number>/", OrderDetailView.as_view(), name="order-detail"),
]