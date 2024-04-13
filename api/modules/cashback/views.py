from django.db.models import Q
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Category, Cashback
from api.modules.cashback.serializers import CashBackSerializer
from api.modules.category.serializers import CategorySerializer
from api.modules.services.gpt import get_structured_cashbacks_from_gpt_api


class CashbackCreateAPIView(views.APIView):

    def post(self, request):
        try:
            # Retrieve data from request
            content = request.data.get("content")
            bank_card_type_id = request.data.get("bank_card_type_id")

            # Validate necessary inputs
            if not content or not bank_card_type_id:
                return Response({"error": "Missing required 'content' or 'bank_card_type_id'."}, status=status.HTTP_400_BAD_REQUEST)

            # Get all categories and serialize them
            categories = Category.objects.all()
            if not categories:
                return Response({"error": "No categories found."}, status=status.HTTP_404_NOT_FOUND)
            category_serializer = CategorySerializer(categories, many=True)

            # Process cashback data
            cashback_data = get_structured_cashbacks_from_gpt_api(content, category_serializer.data)
            if not cashback_data:
                return Response({"error": "Failed to process cashbacks."}, status=status.HTTP_400_BAD_REQUEST)

            # Create cashback and category objects
            cashback_objs = self.create_cashbacks_and_categories(cashback_data, bank_card_type_id)
            if not cashback_objs:
                return Response({"error": "Failed to create cashback entries."}, status=status.HTTP_400_BAD_REQUEST)

            # Serialize and return the newly created cashback objects
            return Response(data=CashBackSerializer(cashback_objs, many=True).data)

        except Exception as e:
            # General exception catch, logging the exception could be added here
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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










