from rest_framework import serializers

from api.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'number', 'expired_date', 'card_type')  # 'user' is deliberately excluded
        read_only_fields = ('id',)

    def create(self, validated_data):
        # Automatically assign the logged-in user as the owner of the card
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
