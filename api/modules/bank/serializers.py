from rest_framework import serializers

from api.models import Bank
from api.modules.bank_card_type.serializers import BankCardTypeListSerializer


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

    def create(self, validated_data):
        return Bank.objects.create(**validated_data)


class BankCoverSerializer(serializers.ModelSerializer):
    cards = BankCardTypeListSerializer(source='bankcardtype_set', many=True, read_only=True)

    class Meta:
        model = Bank
        fields = ['id', 'name', 'description', 'cards']


class BankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name']
