from django.urls import path
from django.urls import include

from api.views import (
    # GoogleLogInAPIView,
    # CallBackAPIView,
    # GoogleCalendarAPIView
    TestAPIView
)

urlpatterns = [
    path('google/calendar', TestAPIView.as_view()),
    path('auth/', include('api.auth.urls'))
]

