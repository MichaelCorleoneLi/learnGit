from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = "__all__"

class UserRegSerializer(serializers.ModelSerializer):

    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False)
    class Meta:
        model = User
        fields = "__all__"