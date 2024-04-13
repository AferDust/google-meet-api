from rest_framework import serializers

from api.models import BankCardType, Cashback


class BankCardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        fields = "__all__"

    def create(self, validated_data):
        return BankCardType.objects.create(**validated_data)


class CashbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = "__all__"


class BankCardTypeSerializerWithCashbackList(serializers.ModelSerializer):
    cashbacks = CashbackSerializer(many=True)

    class Meta:
        model = BankCardType
        fields = "__all__"


class BankCardTypeParsingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        exclude = ['bank']


class BankCardTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        exclude = ['bank', 'url']
