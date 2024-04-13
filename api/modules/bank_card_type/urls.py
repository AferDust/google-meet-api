from rest_framework import routers

from django.urls import path, include
from .views import (
    BankCardTypeModelViewSet,
    BankCardReadonlyModelViewSet
)

bank_card_type_router = routers.SimpleRouter()
bank_card_type_router.register(r'', BankCardTypeModelViewSet)

bank_card_type_readonly_router = routers.SimpleRouter()
bank_card_type_readonly_router.register(r'', BankCardReadonlyModelViewSet, basename='bankcardtype')

urlpatterns = [
    path('', include(bank_card_type_router.urls)),
    path('filters', include(bank_card_type_readonly_router.urls))
]
