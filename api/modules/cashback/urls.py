from rest_framework import routers

from django.urls import path, include

from .views import(
    CashbackCreateAPIView,
    BankCardReadonlyModelViewSet,
    # CategoryCashbackAPIView,
)

bank_card_type_readonly_router = routers.SimpleRouter()
bank_card_type_readonly_router.register(r'', BankCardReadonlyModelViewSet, basename='cashback')

urlpatterns = [
    path('create/', CashbackCreateAPIView.as_view()),
    path('', include(bank_card_type_readonly_router.urls)),
    # path('list/<int:category_id>/', CategoryCashbackAPIView.as_view()),
]
