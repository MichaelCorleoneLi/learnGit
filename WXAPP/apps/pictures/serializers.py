from rest_framework import serializers

from .models import Picture
from wx_user.serializers import UserSerializer


class PicturesSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Picture
        fields = "__all__"