from django.urls import path
from django.urls import include

from api.views import (
    # GoogleLogInAPIView,
    # CallBackAPIView,
    # GoogleCalendarAPIView
    TestAPIView, MyProtectedView
)

urlpatterns = [
    path('google/calendar', TestAPIView.as_view()),
    path('auth/', include('api.auth.urls')),
    path('program/', include('api.modules.program.urls')),

    path('test/googe-acces-token/', MyProtectedView.as_view())
]

