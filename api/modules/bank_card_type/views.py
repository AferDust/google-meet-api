from rest_framework import viewsets, views
from rest_framework.response import Response

from api.models import BankCardType
from .serializers import (
    BankCardTypeParsingListSerializer,
    BankCardTypeSerializer
)
from ..services.gpt import get_structured_cashbacks_from_gpt_api


class BankCardTypeModelViewSet(viewsets.ModelViewSet):
    queryset = BankCardType.objects.all()
    serializer_class = BankCardTypeSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BankCardTypeParsingListSerializer

        return super().get_serializer_class()


class CashbackCreateAPIView(views.APIView):
    def post(self, request):
        content = request.data.get("content")
        print(content)

        # categories =

        cashbacks_data = get_structured_cashbacks_from_gpt_api(content)
        print(cashbacks_data)
        # programs = self.create_program_with_faq(program_data.get("programs"))
        print(cashbacks_data)
        return Response(data=cashbacks_data)
