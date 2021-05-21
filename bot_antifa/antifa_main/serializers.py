from rest_framework import serializers

from antifa_main.models import User


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
