from rest_framework import serializers

from api.models import Cashback


class CashBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = "__all__"
