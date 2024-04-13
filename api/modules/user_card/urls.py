from django.urls import path
from .views import CardListCreateView, CardDestroyView

urlpatterns = [
    path('', CardListCreateView.as_view(), name='list-create-card'),
    path('<int:pk>/', CardDestroyView.as_view(), name='delete-card'),
]
