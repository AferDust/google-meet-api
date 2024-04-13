from django.urls import path

from api.auth.views import (
    GoogleOAuth2AuthorizationAPIView,
    GetUserGoogleTokemAPIView,
    GoogleOAuth2CallbackAPIView,
    RegistrationCreateAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

urlpatterns = [
    path('signin', GoogleOAuth2AuthorizationAPIView.as_view(), name='google-signin'),
    path('callback', GoogleOAuth2CallbackAPIView.as_view(), name='google-signin-callback'),
    path('googe-acces-token', GetUserGoogleTokemAPIView.as_view(), name='get-google-token'),

    path('registration/', RegistrationCreateAPIView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
