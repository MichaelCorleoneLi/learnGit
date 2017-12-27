from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import UserCourse
from .serializers import UserCourseDetailSerializer, UserCourseSerializer


# Create your views here.
class UserCourseViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,
                          mixins.DestroyModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        获取用户学习的课程列表
    retrieve:
        判断某个课程是否已经学习
    create:
        学习课程
    """
    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserCourseDetailSerializer
        elif self.action == "create":
            return UserCourseSerializer

        return UserCourseSerializer