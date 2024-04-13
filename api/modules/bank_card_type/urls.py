from rest_framework import routers

from django.urls import path, include
from .views import BankCardTypeModelViewSet, CashbackCreateAPIView

bank_card_type_router = routers.SimpleRouter()
bank_card_type_router.register(r'', BankCardTypeModelViewSet)

urlpatterns = [
    path('cashback/create/', CashbackCreateAPIView.as_view()),
    path('', include(bank_card_type_router.urls)),
]
