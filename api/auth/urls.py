from django.contrib import admin
from django.urls import path
from django.urls import include

from api.auth.views import (
    GoogleOAuth2AuthorizationAPIView,
    GoogleOAuth2CallbackAPIView
)

urlpatterns = [
    path('signin', GoogleOAuth2AuthorizationAPIView.as_view(), name='google-signin'),
    path('callback', GoogleOAuth2CallbackAPIView.as_view(), name='google-signin-callback')
]