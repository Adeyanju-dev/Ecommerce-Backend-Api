from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView


urlpatterns = [
    path("", CartView.as_view()),
    path("add/", AddToCartView.as_view()),
    path("remove/<int:item_id>/", RemoveFromCartView.as_view()),
]