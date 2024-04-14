from rest_framework import serializers
from api.models import BankCardType


class BankCardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        fields = "__all__"

    def create(self, validated_data):
        return BankCardType.objects.create(**validated_data)


class BankCardTypeParsingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        exclude = ['bank']


class BankCardTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        exclude = ['bank', 'url']
