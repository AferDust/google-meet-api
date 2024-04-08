from django.urls import path
from django.urls import include

from api.views import (
    GoogleLogInAPIView,
    CallBackAPIView,
    GoogleCalendarAPIView
)

urlpatterns = [
    path('google/sign-in', GoogleLogInAPIView.as_view()),
    path('google/callback', CallBackAPIView.as_view()),
    path('google/calendar', GoogleCalendarAPIView.as_view())
]