from rest_framework import serializers

from api.models import Cashback


class CashBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = "__all__"


class BankCardTypeWithCashbackListSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank_card_type.bank.name')
    card_name = serializers.CharField(source='bank_card_type.name')
    category = serializers.SerializerMethodField()

    class Meta:
        model = Cashback
        fields = ['id', 'bank_name', 'card_name', 'category',
                  'percent', 'has_qr_payment', 'has_card_payment']

    def get_category(self, obj):
        if obj.category:
            return obj.category.category

        return None


class BankCardTypeWithCashbackCoverSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank_card_type.bank.name')
    card_name = serializers.CharField(source='bank_card_type.name')
    bank_card_type_url = serializers.URLField(source='bank_card_type.url')
    category = serializers.SerializerMethodField()

    class Meta:
        model = Cashback
        fields = ['id', 'card_name', 'bank_name', 'category',
                  'percent', 'expired_date', 'bank_card_type_url',
                  'has_qr_payment', 'has_card_payment']

    def get_category(self, obj):
        if obj.category:
            return obj.category.category

        return None
