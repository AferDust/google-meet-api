from rest_framework import routers

from django.urls import path
from .views import CashbackCreateAPIView


urlpatterns = [
    path('create/', CashbackCreateAPIView.as_view()),

]
