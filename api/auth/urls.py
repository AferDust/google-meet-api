from django.contrib import admin
from django.urls import path
from django.urls import include

from api.auth.views import (
    GoogleOAuth2AuthorizationAPIView,
    GoogleOAuth2CallbackAPIView, RegistrationCreateAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

urlpatterns = [
    path('signin', GoogleOAuth2AuthorizationAPIView.as_view(), name='google-signin'),
    path('callback', GoogleOAuth2CallbackAPIView.as_view(), name='google-signin-callback'),

    path('registration/', RegistrationCreateAPIView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
