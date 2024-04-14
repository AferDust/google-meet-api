from django.db.models import Q
from rest_framework import viewsets, views

from api.models import BankCardType, Cashback
from .serializers import (
    BankCardTypeParsingListSerializer,
    BankCardTypeSerializer
)


class BankCardTypeModelViewSet(viewsets.ModelViewSet):
    queryset = BankCardType.objects.all()
    serializer_class = BankCardTypeSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BankCardTypeParsingListSerializer

        return super().get_serializer_class()
