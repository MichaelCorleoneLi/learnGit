from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import UserPicture
from .serializers import UserPictureDetailSerializer, UserPictureSerializer


# Create your views here.
class UserPictureViewSet(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                         mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    用户收藏的作品
    """
    def get_queryset(self):
        return UserPicture.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        if self.action == "List":
            return UserPictureDetailSerializer
        elif self.action == "create":
            return UserPictureSerializer
        return UserPictureSerializer