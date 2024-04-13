from rest_framework import viewsets, views
from rest_framework.response import Response

from api.models import BankCardType, Category, Cashback
from .serializers import (
    BankCardTypeParsingListSerializer,
    BankCardTypeSerializer
)
from ..cashback.serializers import CashBackSerializer
from ..category.serializers import CategorySerializer
from ..services.gpt import get_structured_cashbacks_from_gpt_api


class BankCardTypeModelViewSet(viewsets.ModelViewSet):
    queryset = BankCardType.objects.all()
    serializer_class = BankCardTypeSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BankCardTypeParsingListSerializer

        return super().get_serializer_class()

