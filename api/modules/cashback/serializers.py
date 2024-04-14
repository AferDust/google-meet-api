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
        return None
