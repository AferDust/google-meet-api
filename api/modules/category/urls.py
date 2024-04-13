from rest_framework import routers

from django.urls import path, include
from .views import CategoryModelViewSet

category_router = routers.SimpleRouter()
category_router.register(r'', CategoryModelViewSet)

urlpatterns = [
    path('', include(category_router.urls))
]
