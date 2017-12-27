from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserPicture
from pictures.serializers import PicturesSerializer


class UserPictureDetailSerializer(serializers.ModelSerializer):
    picture = PicturesSerializer()

    class Meta:
        model = UserPicture
        fields = "__all__"

class UserPictureSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    picture = PicturesSerializer()

    class Meta:
        model = UserPicture
        validators = [
            UniqueTogetherValidator(
                queryset=UserPicture.objects.all(),
                fields = ('user', 'picture'),
                message = '已收藏'
            )
        ]
        fields = "__all__"