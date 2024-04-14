from django.db.models import Q
from django.core.cache import cache

from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from api.models import Category, Cashback, Card
from api.modules.cashback.serializers import CashbackSerializer, CashbackUserSerializer
from api.modules.cashback.serializers import CashBackSerializer, BankCardTypeWithCashbackCoverSerializer, \
    BankCardTypeWithCashbackListSerializer
from api.modules.category.serializers import CategorySerializer
from api.modules.services.gpt import get_structured_cashbacks_from_gpt_api


class CashbackCreateAPIView(views.APIView):

    def post(self, request):
        try:
            # Retrieve data from request
            print("1")
            content = request.data.get("content")
            bank_card_type_id = request.data.get("bank_card_type_id")
            print("2")

            # Validate necessary inputs
            if not content or not bank_card_type_id:
                return Response({"error": "Missing required 'content' or 'bank_card_type_id'."},
                                status=status.HTTP_400_BAD_REQUEST)
            print("3")


            # Get all categories and serialize them
            categories = Category.objects.all()
            category_serializer = CategorySerializer(categories, many=True)
            print("4")


            # Process cashback data
            cashback_data = get_structured_cashbacks_from_gpt_api(content, category_serializer.data)
            print("5")

            # Create cashback and category objects
            cashback_objs = self.create_cashbacks_and_categories(cashback_data, bank_card_type_id)
            print("6")


            # Serialize and return the newly created cashback objects
            return Response(data=CashBackSerializer(cashback_objs, many=True).data)

        except Exception as e:
            # General exception catch, logging the exception could be added here
            return Response({"error": f"An unexpected error occurred: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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


class CategoryCashbackAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_id=None):
        cashbacks = Cashback.objects.filter(category_id__in=(177, category_id)) \
            .select_related('bank_card_type', 'bank_card_type__bank') \
            .order_by('-percent')
        user_card_type_ids = Card.objects.filter(user=request.user).values_list('card_type_id', flat=True).distinct()

        print(user_card_type_ids)

        user_cashbacks = []
        other_cashbacks = []

        for cashback in cashbacks:
            if cashback.bank_card_type_id in user_card_type_ids:
                user_cashbacks.append(cashback)
            else:
                other_cashbacks.append(cashback)

        user_cashbacks_data = CashbackUserSerializer(user_cashbacks, many=True, context={'request': self.request}).data
        other_cashbacks_data = CashbackSerializer(other_cashbacks, many=True).data

        return Response({
            'user_cashbacks': user_cashbacks_data,
            'other_cashbacks': other_cashbacks_data
        }, status=status.HTTP_200_OK)


class BankCardReadonlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = BankCardTypeWithCashbackListSerializer
    filter_backends = [SearchFilter]
    ordering_fields = ['percent']
    search_fields = ['bank_card_type__name', 'bank_card_type__bank__name']

    def get_queryset(self):
        cashback = cache.get('cashbacks')
        filter_params = {
            'categories': self.request.query_params.getlist("category"),
            'has_qr_payment': self.request.query_params.get("has_qr_payment", None),
            'has_card_payment': self.request.query_params.get("has_card_payment", None),
            'min_percent': self.request.query_params.get("min_percent"),
            'max_percent': self.request.query_params.get("max_percent"),
            'ordering': self.request.query_params.get('ordering')
        }

        if not cashback:
            cashback = Cashback.objects.select_related('category', 'bank_card_type').order_by('-percent')
            cache.set('cashbacks', cashback, 300)

        queryset = cashback
        filters = Q()

        if filter_params['has_qr_payment']:
            has_qr_payment = filter_params['has_qr_payment'].lower() == 'true'
            filters &= Q(has_qr_payment=has_qr_payment)
        if filter_params['has_card_payment']:
            has_card_payment = filter_params['has_card_payment'].lower() == 'true'
            filters &= Q(has_card_payment=has_card_payment)

        if filter_params['categories']:
            filters |= Q(category__id__in=filter_params['categories']) | Q(category__id=177)

        if filter_params['min_percent']:
            filters &= Q(percent__gte=float(filter_params['min_percent']))
        if filter_params['max_percent']:
            filters &= Q(percent__lte=float(filter_params['max_percent']))

        if filter_params['ordering']:
            queryset = queryset.order_by(filter_params['ordering'])

        return queryset.filter(filters)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BankCardTypeWithCashbackCoverSerializer

        return super().get_serializer_class()

    @action(detail=False, methods=['get'], url_path="get_user_cashbacks", permission_classes=[IsAuthenticated])
    def get_user_cashbacks(self, request):
        queryset = self.get_queryset()
        user_card_type_ids = Card.objects.filter(user=request.user).values_list('card_type_id', flat=True).distinct()

        user_cashback = []
        other_cashback = []

        for cashback in queryset:
            if cashback.bank_card_type_id in user_card_type_ids:
                user_cashback.append(cashback)
            else:
                other_cashback.append(cashback)

        user_cashback_data = CashbackUserSerializer(user_cashback, many=True, context={'request': self.request}).data
        other_cashback_data = CashbackSerializer(other_cashback, many=True).data

        return Response({
            'user_cashbacks': user_cashback_data,
            'other_cashbacks': other_cashback_data
        }, status=status.HTTP_200_OK)
