from rest_framework import routers

from django.urls import path, include
from api.modules.bank.views import BankModelViewSet

bank_router = routers.SimpleRouter()
bank_router.register(r'', BankModelViewSet)


urlpatterns = [
    path('', include(bank_router.urls)),
]

