from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("address", "phone_number")


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "profile"]

    def create(self, validated_data):
        profile = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data, username=validated_data.get("email"))

        Profile.objects.create(user=user, **profile)
        return user
