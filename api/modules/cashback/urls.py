from rest_framework import routers

from django.urls import path, include
from .views import CashbackCreateAPIView, BankCardReadonlyModelViewSet

bank_card_type_readonly_router = routers.SimpleRouter()
bank_card_type_readonly_router.register(r'filters', BankCardReadonlyModelViewSet, basename='cashback')

urlpatterns = [
    path('', include(bank_card_type_readonly_router.urls)),
    path('create/', CashbackCreateAPIView.as_view()),
]
