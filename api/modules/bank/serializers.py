from rest_framework import serializers

from api.models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

    def create(self, validated_data):
        return Bank.objects.create(**validated_data)


class BankCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name']
