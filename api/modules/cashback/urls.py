from rest_framework import routers

from django.urls import path
from .views import CashbackCreateAPIView, CategoryCashbacksAPIView

urlpatterns = [
    path('create/', CashbackCreateAPIView.as_view()),
    path('list/<int:category_id>/', CategoryCashbacksAPIView.as_view()),

]
