from rest_framework import serializers

from api.models import CashBack


class CashBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashBack
        fields = "__all__"
