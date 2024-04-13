from rest_framework import routers

from django.urls import path, include
from .views import BankCardTypeModelViewSet, CashbackCreateAPIView

bank_card_type = routers.SimpleRouter()
bank_card_type.register(r'', BankCardTypeModelViewSet)

urlpatterns = [
    path('', include(bank_card_type.urls)),
    path('cashback/create/', CashbackCreateAPIView.as_view()),
]
