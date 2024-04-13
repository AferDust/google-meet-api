from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Card


class UserCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class CardSerializer(serializers.ModelSerializer):
    user = UserCoverSerializer(read_only=True)

    class Meta:
        model = Card
        fields = ('id', 'number', 'expired_date', 'card_type', "user")  # 'user' is deliberately excluded
        read_only_fields = ('id',)

    def create(self, validated_data):
        # Automatically assign the logged-in user as the owner of the card
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
