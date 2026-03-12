from django.urls import path
from .views import InitiatePaymentView, VerifyPaymentView

urlpatterns = [
    path("initiate/<str:order_number>/", InitiatePaymentView.as_view()),
    path("verify/<str:payment_reference>/", VerifyPaymentView.as_view()),
]