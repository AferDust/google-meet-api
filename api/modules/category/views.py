from rest_framework import viewsets

from api.models import Category
from .serializers import CategorySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

