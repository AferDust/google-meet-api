from django.db.models import Q

from rest_framework import views
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter


from api.models import Category, Cashback
from api.modules.cashback.serializers import CashBackSerializer, BankCardTypeWithCashbackCoverSerializer, \
    BankCardTypeWithCashbackListSerializer
from api.modules.category.serializers import CategorySerializer
from api.modules.services.gpt import get_structured_cashbacks_from_gpt_api


class CashbackCreateAPIView(views.APIView):

    def post(self, request):
        content = request.data.get("content")
        bank_card_type_id = request.data.get("bank_card_type_id")

        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)

        cashback_data = get_structured_cashbacks_from_gpt_api(content, category_serializer.data)
        cashback_objs = self.create_cashbacks_and_categories(cashback_data, bank_card_type_id)

        return Response(data=CashBackSerializer(cashback_objs, many=True).data)

    def create_cashbacks_and_categories(self, cashbacks_data, bank_card_type_id):
        cashbacks = cashbacks_data.get('cashbacks', [])
        cashback_objs = []

        for cashback_data in cashbacks:
            if isinstance(cashback_data['category'], int):
                category, created = Category.objects.get_or_create(pk=cashback_data['category'])
            else:
                category, created = Category.objects.get_or_create(category=cashback_data['category'])

            try:
                cashback = Cashback.objects.create(
                    percent=cashback_data['percent'],
                    expired_date=cashback_data.get('expired_date'),
                    category=category,
                    bank_card_type_id=bank_card_type_id
                )
            except:
                Cashback.objects.filter(category=category,
                                        bank_card_type_id=bank_card_type_id).delete()
                cashback = Cashback.objects.create(
                    percent=cashback_data['percent'],
                    expired_date=cashback_data.get('expired_date'),
                    category=category,
                    bank_card_type_id=bank_card_type_id
                )

            cashback_objs.append(cashback)
        return cashback_objs


class BankCardReadonlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = BankCardTypeWithCashbackListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['percent']
    search_fields = ['bank_card_type__name', 'bank_card_type__bank__name']

    def get_queryset(self):
        filter_params = {
            'categories': self.request.query_params.getlist("category"),
            'has_qr_payment': self.request.query_params.get("has_qr_payment", 'true').lower() == 'true',
            'has_card_payment': self.request.query_params.get("has_card_payment", 'true').lower() == 'true',
            'min_percent': self.request.query_params.get("min_percent"),
            'max_percent': self.request.query_params.get("max_percent"),
        }

        queryset = Cashback.objects.all()
        filters = Q()

        print(filter_params['has_card_payment'])
        print(filter_params['has_qr_payment'])

        filters &= Q(has_qr_payment=filter_params['has_qr_payment'])
        filters &= Q(has_card_payment=filter_params['has_card_payment'])

        if filter_params['categories']:
            filters |= Q(category__id__in=filter_params['categories'])

        if filter_params['min_percent']:
            filters &= Q(percent__gte=float(filter_params['min_percent']))
        if filter_params['max_percent']:
            filters &= Q(percent__lte=float(filter_params['max_percent']))

        return queryset.filter(filters)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BankCardTypeWithCashbackCoverSerializer

        return super().get_serializer_class()







