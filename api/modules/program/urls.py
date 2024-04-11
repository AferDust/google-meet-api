from django.urls import path

from api.modules.program.views import ProgramWithFAQAPIView

urlpatterns = [
    path('create/', ProgramWithFAQAPIView.as_view()),
]

