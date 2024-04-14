from rest_framework import serializers

from api.models import Cashback


class CashBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = "__all__"


class CashbackSerializer(serializers.ModelSerializer):
    bank_card_type = serializers.SerializerMethodField()
    bank = serializers.SerializerMethodField()

    class Meta:
        model = Cashback
        fields = ['id', 'bank', 'bank_card_type', 'percent', 'has_qr_payment', 'has_card_payment']

    def get_bank_card_type(self, obj):
        return obj.bank_card_type.name

    def get_bank(self, obj):
        return obj.bank_card_type.bank.name


class CashbackUserSerializer(serializers.ModelSerializer):
    bank_card_type = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    # card_number = serializers.SerializerMethodField()
    bank = serializers.SerializerMethodField()

    class Meta:
        model = Cashback
        fields = ['id', 'bank', 'bank_card_type', 'user_name', 'percent', 'has_qr_payment', 'has_card_payment']

    def get_bank_card_type(self, obj):
        return obj.bank_card_type.name

    def get_bank(self, obj):
        return obj.bank_card_type.bank.name
    # def get_card_number(self, obj):
    #     return obj.bank_card_type.bank.name

    def get_user_name(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            return request.user.first_name + " " + request.user.last_name

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
