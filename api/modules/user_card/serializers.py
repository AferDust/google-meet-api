from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Card


class UserCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class CardSerializer(serializers.ModelSerializer):
    # user = UserCoverSerializer(read_only=True)
    card_type_name = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Card
        fields = (
        'id', 'number', 'expired_date', 'card_type', "card_type_name", "name")  # 'user' is deliberately excluded
        read_only_fields = ('id',)

    def get_card_type_name(self, obj):
        return obj.card_type.name
    def get_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    def create(self, validated_data):
        # Automatically assign the logged-in user as the owner of the card
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
