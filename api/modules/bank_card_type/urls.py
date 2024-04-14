from rest_framework import routers

from django.urls import path, include
from .views import BankCardTypeModelViewSet

bank_card_type_router = routers.SimpleRouter()
bank_card_type_router.register(r'', BankCardTypeModelViewSet)

urlpatterns = [
    path('', include(bank_card_type_router.urls)),
]
