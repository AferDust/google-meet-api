from rest_framework.viewsets import ModelViewSet

from api.models import Bank
from api.modules.bank.serializers import (
    BankSerializer,
    BankCoverSerializer
)


class BankModelViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BankCoverSerializer

        return super().get_serializer_class()