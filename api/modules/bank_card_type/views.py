from django.db.models import Q
from rest_framework import viewsets, views

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from api.models import BankCardType, Cashback
from .serializers import (
    BankCardTypeParsingListSerializer,
    BankCardTypeSerializer,
    BankCardTypeWithCashbackListSerializer,
    BankCardTypeWithCashbackCoverSerializer
)


class BankCardTypeModelViewSet(viewsets.ModelViewSet):
    queryset = BankCardType.objects.all()
    serializer_class = BankCardTypeSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BankCardTypeParsingListSerializer

        return super().get_serializer_class()


class BankCardReadonlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = BankCardTypeWithCashbackListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['percent']
    search_fields = ['bank_card_type__name', 'bank_card_type__bank__name']

    def get_queryset(self):
        filter_params = {
            'categories': self.request.query_params.getlist("category"),
            'has_qr_payment': self.request.query_params.get("has_qr_payment", 'false').lower() == 'true',
            'has_card_payment': self.request.query_params.get("has_card_payment", 'false').lower() == 'true',
            'min_percent': self.request.query_params.get("min_percent"),
            'max_percent': self.request.query_params.get("max_percent"),
        }

        queryset = Cashback.objects.all()
        filters = Q()

        if filter_params['categories']:
            filters &= Q(category__id__in=filter_params['categories'])

        if filter_params['has_qr_payment']:
            filters &= Q(has_qr_payment=True)
        if filter_params['has_card_payment']:
            filters &= Q(has_card_payment=True)

        if filter_params['min_percent']:
            min_percent = float(filter_params['min_percent'])
            filters &= Q(percent__gte=min_percent)
        if filter_params['max_percent']:
            max_percent = float(filter_params['max_percent'])
            filters &= Q(percent__lte=max_percent)  #

        return queryset.filter(filters)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BankCardTypeWithCashbackCoverSerializer

        return super().get_serializer_class()
