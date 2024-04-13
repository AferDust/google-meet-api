from rest_framework import serializers

from api.models import BankCardType, Cashback
from api.modules.cashback.serializers import CashBackSerializer


class BankCardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        fields = "__all__"

    def create(self, validated_data):
        return BankCardType.objects.create(**validated_data)


class BankCardTypeWithCashbackListSerializer(serializers.ModelSerializer):
    bank_card_type_name = serializers.CharField(source='bank_card_type.name')
    category = serializers.SerializerMethodField()
    method = serializers.SerializerMethodField()

    class Meta:
        model = Cashback
        fields = ['id', 'bank_card_type_name', 'percent',
                  'category_category', 'method_method']

    def get_category(self, obj):
        if obj.method:
            return obj.method.method

        return None

    def get_category(self, obj):
        if obj.category:
            return obj.category.category

        return None


class BankCardTypeWithCashbackCoverSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank_card_type.bank.name')
    bank_card_type_name = serializers.CharField(source='bank_card_type.name')
    bank_card_type_url = serializers.URLField(source='bank_card_type_url')
    category_category = serializers.CharField(source='category.category')
    method_method = serializers.CharField(source='method.method')

    class Meta:
        model = Cashback
        fields = ['id', 'bank_card_type_name', 'percent', 'bank_name',
                  'category_category', 'method_method',
                  'expired_date', 'bank_card_type_url', ]


class BankCardTypeParsingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        exclude = ['bank']


class BankCardTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCardType
        exclude = ['bank', 'url']
